"""FROM SQUAD_V2"""


import json

import datasets
from datasets.tasks import QuestionAnsweringExtractive


# TODO(squad_v2): BibTeX citation
_CITATION = """\
Tuora, R., Zawadzka-Paluektau, N., Klamra, C., Zwierzchowska, A., Kobyliński, Ł. (2022). 
Towards a Polish Question Answering Dataset (PoQuAD). 
In: Tseng, YH., Katsurai, M., Nguyen, H.N. (eds) From Born-Physical to Born-Virtual: Augmenting Intelligence in Digital Libraries. ICADL 2022. 
Lecture Notes in Computer Science, vol 13636. Springer, Cham. 
https://doi.org/10.1007/978-3-031-21756-2_16
"""

_DESCRIPTION = """\
PoQuaD description
"""


_URLS = {
    "train": "poquad-train.json",
    "dev": "poquad-dev.json",
}


class SquadV2Config(datasets.BuilderConfig):
    """BuilderConfig for SQUAD."""

    def __init__(self, **kwargs):
        """BuilderConfig for SQUADV2.
        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(SquadV2Config, self).__init__(**kwargs)


class SquadV2(datasets.GeneratorBasedBuilder):
    """TODO(squad_v2): Short description of my dataset."""

    # TODO(squad_v2): Set up version.
    BUILDER_CONFIGS = [
        SquadV2Config(name="poquad", version=datasets.Version("1.0.0"), description="PoQuaD plaint text"),
    ]

    def _info(self):
        # TODO(squad_v2): Specifies the datasets.DatasetInfo object
        return datasets.DatasetInfo(
            # This is the description that will appear on the datasets page.
            description=_DESCRIPTION,
            # datasets.features.FeatureConnectors
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "title": datasets.Value("string"),
                    "context": datasets.Value("string"),
                    "question": datasets.Value("string"),
                    "answers": datasets.features.Sequence(
                        {
                            "text": datasets.Value("string"),
                            "answer_start": datasets.Value("int32"),
                        }
                    ),
                    # These are the features of your dataset like images, labels ...
                }
            ),
            # If there's a common (input, target) tuple from the features,
            # specify them here. They'll be used if as_supervised=True in
            # builder.as_dataset.
            supervised_keys=None,
            # Homepage of the dataset for documentation
            homepage="https://rajpurkar.github.io/SQuAD-explorer/",
            citation=_CITATION,
            task_templates=[
                QuestionAnsweringExtractive(
                    question_column="question", context_column="context", answers_column="answers"
                )
            ],
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        # TODO(squad_v2): Downloads the data and defines the splits
        # dl_manager is a datasets.download.DownloadManager that can be used to
        # download and extract URLs
        urls_to_download = _URLS
        downloaded_files = dl_manager.download_and_extract(urls_to_download)

        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": downloaded_files["train"]}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"filepath": downloaded_files["dev"]}),
        ]

    def _generate_examples(self, filepath):
        """Yields examples."""
        # TODO(squad_v2): Yields (key, example) tuples from the dataset
        with open(filepath, encoding="utf-8") as f:
            squad = json.load(f)
            id_ = 0
            for example in squad["data"]:
                title = example.get("title", "")
                # paragraph_id = example["id"]
                for paragraph in example["paragraphs"]:
                    context = paragraph["context"]  # do not strip leading blank spaces GH-2585
                    for qa in paragraph["qas"]:
                        question = qa["question"]

                        if "answers" not in qa:
                            continue
                        answer_starts = [answer["answer_start"] for answer in qa["answers"]]
                        answers = [answer['generative_answer'] for answer in qa["answers"]]
                        # is_impossible = qa["is_impossible"]
                        # Features currently used are "context", "question", and "answers".
                        # Others are extracted here for the ease of future expansions.
                        id_ += 1
                        yield str(id_), {
                            "id": str(id_),
                            "title": title,
                            "context": context,
                            "question": question,
                            #"is_impossible" : is_impossible,
                            # "paragraph_id": paragraph_id,
                            "answers": {
                                "answer_start": answer_start,
                                "text": answers,
                            },
                        }