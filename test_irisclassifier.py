from typing import Set
from irisclassifier import IrisClassifier
import pytest
import irisclassifier
def test_ingestion():
    assert False


def test_evaluation():
    i = irisclassifier.IrisClassifier()
    i.ingestion()
    i.segregation()
    i.train()
    res = i.evaluation()
    assert res>0.75
