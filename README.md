# 用rasa_nlu 和 rasa_core 构建对话机器人。

## 环境安装

```bash
pip install git+https://github.com/mit-nlp/MITIE.git
pip install rasa_nlu rasa_core
```

## 训练nlu模型

首先构建固定格式的文档，可以是markdown格式, 也可以是json格式。如[nlu.md](config/nlu/nlu.md), 以及[nlu.json]config/nlu/nlu.json) 。

然后运行[nlu_model.py](nlu_model.py), 命令`python nlu_model.py`

运行后，生成nlu模型在文件夹 `models/nlu/default/current` 下。

## 训练对话管理模型

训练对话管理，需要预先定义好 `domain` 和 `stories`，也即预先定义好领域和故事。

domain是yaml格式，如[domain.yml](config/domain/domain.yml), story是markdown格式，如[stories_en.md](config/domain/stories_en.md)

接下来，运行[dm_model.py](dm_model.py)， 命令`python dm_model.py`

训练完毕，生成的模型在`models/dialogue/`下。

## 模型启动

训练好nlu模型，我们可以得到问句的意图和实体（如果问题中存在预先定义好的实体的话），训练好对话管理模型，我们可以根据意图获取到action, 然后用action获取到答案或者作出相应的动作。

运行[run_bot.py](run_bot.py), 即可在终端进行对话。

运行[run_server_bot.py](run_server_bot.py), 可以通过调用api的形式对话。

## 自定义action

在实际的对话项目中，对某些问题，我们可以给出回复，但是对于一些任务型，如智能音箱中的`放首歌`，我们可以设计自己的actin, 格式如[actions.py](apis/actions.py) 所示，继承自rasa_core提供的`Action`类，实现方法即可。

但是光自定义action还不行，还需要让action生效，即运行`start_actions.py`，即可以使用自定义action了。