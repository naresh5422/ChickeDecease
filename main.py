from CNNClassifier import logger
from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNNClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CNNClassifier.pipeline.stage_03_training import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} is completed <<<<<<<<\n\nX========X")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f"*******************")
    logger.info(f">>>----- Stage {STAGE_NAME} is started-----<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>------ Stage {STAGE_NAME} is completed-------<<<<<<\n\n X=======X")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Training"

try:
    logger.info(f"*******************")
    logger.info(f">>>----- Stage {STAGE_NAME} is started-----<<<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>------ Stage {STAGE_NAME} is completed-------<<<<<<\n\n X=======X")
except Exception as e:
    logger.exception(e)
    raise e