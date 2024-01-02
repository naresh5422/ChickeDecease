import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from CNNClassifier.utils.common import decodeImage
from CNNClassifier.pipeline.prediction import PredictionPipeline


os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", )
