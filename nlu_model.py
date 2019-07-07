from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter
import json


# natural language understanding model
def train_nlu(data='./config/nlu/nlu.md',
              configs='./config/pipeline/spacy_en.yml',
              model_dir='./models/nlu'):
    training_data = load_data(data)
    trainer = Trainer(config.load(configs))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name='current')
    print(model_directory)


def pprint(o):
    print(json.dumps(o, indent=2, ensure_ascii=False))


def run_nlu(nlu_model_path='./models/nlu/default/current'):
    interpreter = Interpreter.load(nlu_model_path)
    pprint(interpreter.parse(u"上海明天天气"))


if __name__ == '__main__':
    # train_nlu('./config/nlu/nlu.md', './config/pipeline/spacy_en.yml', './models/nlu')
    train_nlu('./config/nlu/nlu.json', './config/pipeline/MITIE+jieba.yml', './models/nlu_zh')
    run_nlu(nlu_model_path='./models/nlu_zh/default/current')
