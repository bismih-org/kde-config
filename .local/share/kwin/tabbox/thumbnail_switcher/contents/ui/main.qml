/*************
    KWin - the KDE window manager

    This tab switcher is a modification of the original thumbnail switcher written by Martin Gräßlin


    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

*********************************************************************/

import QtQuick 2.0
import QtQuick.Layouts 1.15
import org.kde.plasma.core 2.0 as PlasmaCore
import org.kde.plasma.components 3.0 as PlasmaComponents3
import org.kde.kwin 2.0 as KWin

KWin.Switcher {
    id: tabBox
    currentIndex: thumbnailListView.currentIndex
    PlasmaCore.Dialog {
        id: dialog
        location: PlasmaCore.Types.Floating
        visible: tabBox.visible
        flags: Qt.X11BypassWindowManagerHint
        x: tabBox.screenGeometry.x + tabBox.screenGeometry.width * 0.5 - dialogMainItem.width * 0.5
        y: tabBox.screenGeometry.y + tabBox.screenGeometry.height * 0.5 - dialogMainItem.height * 0.5
        mainItem: Item {
            id: dialogMainItem
            property real screenFactor: tabBox.screenGeometry.width/tabBox.screenGeometry.height
            property int optimalWidth: (thumbnailListView.thumbnailWidth + hoverItem.margins.left + hoverItem.margins.right) * thumbnailListView.count
            property int optimalHeight: thumbnailListView.thumbnailWidth + hoverItem.margins.top + hoverItem.margins.bottom

            width: Math.min(Math.max(0, optimalWidth), tabBox.screenGeometry.width * 0.9)
            height: Math.min(Math.max(0, optimalHeight), tabBox.screenGeometry.height * 0.5)
            clip: true
            focus: true
            // just to get the margin sizes
            PlasmaCore.FrameSvgItem {
                id: hoverItem
                imagePath: "widgets/viewitem"
                prefix: "hover"
                visible: false
            }

            ListView {
                id: thumbnailListView
                model: tabBox.model
                orientation: ListView.Horizontal
                property int thumbnailWidth: 200 * PlasmaCore.Units.devicePixelRatio
                property int iconSize: PlasmaCore.Units.iconSizes.medium
                height: thumbnailWidth
                width: Math.min(parent.width - (anchors.leftMargin + anchors.rightMargin) - (hoverItem.margins.left + hoverItem.margins.right), thumbnailWidth * count + 5 * (count - 1))
                spacing: PlasmaCore.Units.smallSpacing
                highlightMoveDuration: 0
                highlightResizeDuration: 0
                anchors {
                    verticalCenter: parent.verticalCenter
                    horizontalCenter: parent.horizontalCenter
                }
                clip: true
                delegate: Item {
                    property alias caption: thumbnailItem.caption
                    property alias icon: thumbnailItem.icon
                    id: delegateItem
                    width: thumbnailListView.thumbnailWidth
                    height: thumbnailListView.thumbnailWidth

                    MouseArea {
                        anchors.fill: parent
                        onClicked: {
                            thumbnailListView.currentIndex = index;
                        }
                    }

                    Item {
                        property variant caption: model.caption
                        property variant icon: model.icon
                        id: thumbnailItem
                        anchors {
                            fill: parent
                        }


                        ColumnLayout {
                            z: 0
                            spacing: 0
                            anchors.fill: parent
                            anchors.leftMargin: hoverItem.margins.left
                            anchors.topMargin: hoverItem.margins.top
                            anchors.rightMargin: hoverItem.margins.right
                            anchors.bottomMargin: hoverItem.margins.bottom

                            // KWin.ThumbnailItem needs a container
                            // otherwise it will be drawn the same size as the parent ColumnLayout
                            Item {
                                Layout.fillWidth: true
                                Layout.fillHeight: true
                                Layout.topMargin: 5
                                Layout.bottomMargin: 5

                                // Cannot draw anything (like an icon) on top of thumbnail
                                KWin.ThumbnailItem {
                                    anchors.fill: parent
                                    wId: windowId
                                }


                                PlasmaCore.IconItem {
                                    z: 1
                                    id: iconItem
                                    anchors {

                                            horizontalCenter: parent.horizontalCenter
                                            bottom: parent.bottom
                                            bottomMargin: hoverItem.margins.bottom
                                    }
                                    width: thumbnailListView.iconSize
                                    height: thumbnailListView.iconSize
                                    source: model.icon
                                    usesPlasmaTheme: false
                                }
                            }



                            PlasmaComponents3.Label {
                                id: label
                                Layout.fillWidth: true
                                Layout.topMargin: 5
                                horizontalAlignment: Text.AlignHCenter
                                text: model.caption
                                elide: Text.ElideRight
                            }
                        }
                    }
                }
                highlight: PlasmaCore.FrameSvgItem {
                    id: highlightItem
                    imagePath: "widgets/viewitem"
                    prefix: "hover"
                    width: thumbnailListView.thumbnailWidth
                    height: thumbnailListView.thumbnailWidth*(1.0/dialogMainItem.screenFactor)
                }
                boundsBehavior: Flickable.StopAtBounds
                Connections {
                    target: tabBox
                    function onCurrentIndexChanged() {thumbnailListView.currentIndex = tabBox.currentIndex;}
                }
            }

            /*
            * Key navigation on outer item for two reasons:
            * @li we have to emit the change signal
            * @li on multiple invocation it does not work on the list view. Focus seems to be lost.
            **/
            Keys.onPressed: {
                if (event.key == Qt.Key_Left) {
                    thumbnailListView.decrementCurrentIndex();
                } else if (event.key == Qt.Key_Right) {
                    thumbnailListView.incrementCurrentIndex();
                }
            }
        }
    }
}
