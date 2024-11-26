class Config:
    def __init__(
        self,
        id_: int,
        file: str,
        file_path: str,
        index: int,
        file_name: tuple,
        is_folder_need: bool = False,
    ) -> None:
        self.id_ = id_
        self.file = file
        self.file_path = file_path
        self.file_name = file_name
        self.is_compressed = file.endswith((".tar.xz", ".tar.gz", ".plasmoid"))
        self.index = index
        self.is_folder = is_folder_need

ids = [
            Config(
                id_=1901768,
                file="Utterly-Round-Desktop.tar.xz",
                file_path="usr/share/plasma/desktoptheme/",
                file_name=("Utterly-Round"),
                index=1,
                is_folder_need=True,
            ),
            Config(
                id_=2011605,
                file="Utterly-Round-Desktop-Solid.tar.xz",
                file_path="usr/share/plasma/desktoptheme/",
                file_name=("Utterly-Round-Solid"),
                index=1,
                is_folder_need=True,
            ),
            Config(
                id_=1457141,
                file="Future-cursors.tar.gz",
                file_path="usr/share/icons/",
                file_name=("Future-cursors"),
                index=1,
                is_folder_need=False
            ),
            Config(
                id_=1465392,
                file="Future-cyan-cursors.tar.gz",
                file_path="usr/share/icons/",
                file_name=("Future-cyan-cursors"),
                index=1,
                is_folder_need=False,
            ),
            Config(
                id_=2148021,
                file="blueberry.colors",
                file_path="usr/share/color-schemes/",
                file_name=("blueberry.colors"),
                index=1,
                is_folder_need=False,
            ),
            Config(
                id_=1477945,
                file="Fluent-orange.tar.xz",
                file_path="usr/share/plasma/desktoptheme/",
                index=4,
                file_name=("Fluent-orange","Fluent-orange-dark","Fluent-orange-light"),
                is_folder_need=False,
            ),
            Config(
                id_=2203672,
                file="HelixAI.plasmoid",
                file_path="usr/share/plasma/plasmoids/",
                file_name=("com.mrgovinddubey.helixAI"),
                index=1,
                is_folder_need=False,
            ),
            Config(
                id_=998901,
                file="eventcalendar-v76-plasma5.13.plasmoid",
                file_path="usr/share/plasma/plasmoids/",
                file_name=("org.kde.plasma.eventcalendar"),
                index=1,
                is_folder_need=True,
            ),
            Config(
                id_=1570454,
                file="energy.monitor.plasmoid",
                file_path="usr/share/plasma/plasmoids/",
                file_name=("energy.monitor"),
                index=1,
                is_folder_need=False,
            ),
            Config(
                id_=2103591,
                file="Clock.Asitoki.Color.tar.xz",
                file_path="usr/share/plasma/plasmoids/",
                file_name=("Clock.Asitoki.Color"),
                index=1,
            ),
        ]


