import logging
from logging.config import dictConfig

from src.utils.config import Config
import src.project_name.preparation.dataloader as dal
import src.project_name.training.trainingpipe as smp
import src.project_name.preprocess.preprocesspipe as sbp


def main() -> None:
    """
    Runs the pipeline
    """

    config = "config_test.yml"
    try:
        config = Config(config)
    except FileNotFoundError:
        print("configuration file: %s not found" % config, file=sys.stderr)
        sys.exit(1)

    dictConfig(config.get("logging"))

    # Initialize Data Loader
    dl = dal.DataLoader(config)

    # Read csv
    data = dl.get_data()

    # Run Sum Pipeline
    sump = smp.TrainingPipe(config)
    data = sump.transform(data)

    # Run Subtract Pipeline
    subp = sbp.PreprocessPipe(config)
    data = subp.transform(data)

    # Save csv
    dl.save_csv(data)


if __name__ == '__main__':
    main()
