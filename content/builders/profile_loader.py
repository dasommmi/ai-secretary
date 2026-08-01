from pathlib import Path
import yaml


class ProfileLoader:


    @staticmethod
    def load(
            name: str = "sandy"
    ):

        path = (
                Path(__file__)
                .parent.parent
                / "profile"
                / f"{name}.yaml"
        )


        with open(
                path,
                encoding="utf-8"
        ) as file:

            return yaml.safe_load(file)