# Foundation Models For Data Wrangling

This is forked from the [official repo](https://github.com/HazyResearch/fm_data_tasks) for [Can Foundation Models Wrangle Your Data?](<https://arxiv.org/abs/2205.09911>), which appeared in VLDB'23.

We aim to evaluate fairness of the results of using foundation models for data imputation and maybe error detection.

For this purpose, we extend this module with a subset of the [`folktables`](https://github.com/socialfoundations/folktables) dataset.

## Install

Install:

```shell
python3.9 -m venv venv
source venv/bin/activate
pip install -U pip
pip install .
```

Download and unpack the data:

```shell
mkdir data
wget https://fm-data-tasks.s3.us-west-1.amazonaws.com/datasets.tar.gz -P data
tar xvf data/datasets.tar.gz -C data/
```

## Setup

You need to set your OpenAI key to run GPT inference. We also let you change where the datasets are downloaded in case you want to run the code on other data. We use the environment variables

```shell
export OPENAI_API_KEY="<YOU API KEY>"
export DATASET_PATH="$PWD/data/datasets"
```

## Run

To run inference, use

```shell
python -m fm_data_tasks.run_inference --help
```

To see options. Importantly, the `--dry_run` flag will print out examples but not query OpenAI.

We cache all inputs/outputs in sqlite for the ability to rerun without having to require OpenAI. To override the cache add the `--overwrite_cache` flag.

To see a full set of scripts with output results for 200 examples samples of each dataset, see [scripts/run_results.zsh](scripts/run_results.zsh).

Some examples are as follows.

To dry run run 10 examples for Fodors Zagats entity matching with random selection of 3 examples to add to the prompt,

```shell
python -m fm_data_tasks.run_inference \
    --dry_run \
    --num_run 10 \
    --k 3 \
    --sample_method random \
    --data_dir data/datasets/entity_matching/structured/Fodors-Zagats
```

To run 100 examples for 3 trials for Restaurant data imputation on the test data with manual prompt selection,

```shell
python -m fm_data_tasks.run_inference \
    --num_run 100 \
    --num_trials 3 \
    --do_test \
    --sample_method manual \
    --data_dir data/datasets/data_imputation/Restaurant
```
