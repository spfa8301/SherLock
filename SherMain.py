from pyspark.ml.regression import GeneralizedLinearRegression
from pyspark.ml.classification import LogisticRegression
from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import OneHotEncoder
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StandardScaler
from pyspark.ml import Pipeline
import pandas as pd
import numpy as np
import sklearn
import pandas as pd
from pyspark.ml.linalg import Vectors
from pyspark.ml.stat import Correlation
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.classification import GBTClassifier
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql.functions import translate
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import rand,when
from pyspark.ml.feature import VectorAssembler
from pyspark.ml import Pipeline
from pyspark.ml.regression import GBTRegressor
from pyspark.ml.feature import VectorIndexer
from pyspark.ml.evaluation import RegressionEvaluator    
import pyspark.sql.functions as func


def Pepe(D):

    
    spark = SparkSession.builder.master('local[2]').config("spark.executor.memory", "1g").config("spark.driver.memory", "1g").appName('spark_sh_data').getOrCreate()
    df = spark.read.options(header=None, nullValue='NULL', inferSchema=True).option('nullValue','null').csv(D)
    
    newDf = df.withColumn('_c4', translate('_c4', 'NULL', '')).withColumn('_c5', translate('_c5', 'NULL', '')).withColumn('_c6', translate('_c6', 'NULL', '')).withColumn('_c7', translate('_c7', 'NULL', ''))\
        .withColumn('_c8', translate('_c8', 'NULL', ''))
    newDf1 = newDf.withColumn('_c4', newDf["_c4"].cast(IntegerType())).withColumn('_c5', newDf["_c5"].cast(IntegerType())).withColumn('_c6', newDf["_c6"].cast(IntegerType())).withColumn('_c7', newDf["_c7"].cast(IntegerType()))\
        .withColumn('_c8', newDf["_c8"].cast(IntegerType()))
    
    
    data= newDf1.withColumn('rand', when(rand() > 0.5, 'yes').otherwise('no'))
    
    stringIndexer = StringIndexer().setInputCol("_c25").setOutputCol("_c25_index").setHandleInvalid("skip")
    _c25_index_model=stringIndexer.fit(data)
    _c25_index_df=_c25_index_model.transform(data)
    
    encoder = OneHotEncoder().setInputCols(["_c25_index"]).setOutputCols(["_c25_encoded"])
    encoder_model=encoder.fit(_c25_index_df)
    encoder_df=encoder_model.transform(_c25_index_df)

    assembler = VectorAssembler().setInputCols(['_c4','_c5','_c6','_c7','_c8','_c9','_c10','_c11','_c12','_c13','_c14','_c15','_c16','_c17','_c18','_c19','_c20','_c21','_c22','_c23','_c24'])\
                        .setOutputCol("vectorized_features")\
                            .setHandleInvalid("skip")
    assembler_df = assembler.transform(encoder_df)
    
    label_indexer = StringIndexer().setInputCol("rand").setOutputCol("label")
    label_indexer_model=label_indexer.fit(assembler_df)
    label_indexer_df = label_indexer_model.transform(assembler_df)
    
    scaler = StandardScaler().setInputCol("vectorized_features").setOutputCol("features")
    scaler_model=scaler.fit(label_indexer_df)
    scaler_df = scaler_model.transform(label_indexer_df)
    
    pipeline_stages=Pipeline().setStages([stringIndexer,encoder,assembler,label_indexer,scaler])
    pipeline_model=pipeline_stages.fit(data)
    pipeline_df=pipeline_model.transform(data)
    
    print('We working BB')
    return pipeline_df
    


def SherLog(PepePipe):
    train, test = PepePipe.randomSplit([0.8,0.2], seed=56)
    
    lr = LogisticRegression(featuresCol = 'features', labelCol = 'label', maxIter=5)
    lrModel = lr.fit(train)
    predictions = lrModel.transform(test)
    
    return predictions



def MoriarTree(PepePipe):
    train, test = PepePipe.randomSplit([0.8,0.2], seed=56) 
    gbt = GBTRegressor(featuresCol = "features", maxIter=10)
    gbtModel = gbt.fit(train)
    preds = gbtModel.transform(test)
    BiPred = preds.withColumn("preds", func.round(preds["prediction"]).cast('integer'))
    
    return BiPred