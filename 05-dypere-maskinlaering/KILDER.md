# Kilder og datasett

Kurskoden er skrevet som små undervisningseksempler. Offisiell dokumentasjon
forklarer API-ene; originalarbeider og datasettbeskrivelser gir bakgrunnen.
Bruk oppdatert installasjonsvelger for maskinen fremfor en gammel CUDA-kommando.

## Oppsett og PyTorch

- [PyTorchs installasjonsvelger](https://pytorch.org/get-started/locally/) gir sammenhengende valg av pakker, Python og beregningsplattform.
- [NVIDIAs CUDA på WSL](https://docs.nvidia.com/cuda/wsl-user-guide/index.html) forklarer Windows-driver og WSL2.
- [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) dekker tensorer, data, autograd, trening og lagring.
- [CrossEntropyLoss](https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html) beskriver logits og målformat.
- [MultiheadAttention](https://docs.pytorch.org/docs/stable/generated/torch.nn.MultiheadAttention.html) beskriver masker og lagformer. Maskekonvensjoner kan være ulike i andre API-er.
- [JupyterLabs brukerhåndbok](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html) forklarer notatbøker og kernel.

## Bilder

- [Fashion-MNIST fra Zalando Research](https://github.com/zalandoresearch/fashion-mnist) beskriver 60 000 treningsbilder og 10 000 testbilder, 28 × 28 gråtoner, ti kategorier. Repoet angir MIT-lisens.
- [CIFAR-10 fra Alex Krizhevsky](https://www.cs.toronto.edu/~kriz/cifar.html) beskriver 50 000 treningsbilder og 10 000 testbilder, 32 × 32 farger, ti kategorier. Last ned via Torchvision i øvelsen og bruk originalkilden ved annen bruk eller videre distribusjon.
- [Torchvisions ResNet18](https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.resnet18.html) beskriver vekter og forventet forbehandling.
- [PyTorchs overføringslæring](https://docs.pytorch.org/tutorials/beginner/transfer_learning_tutorial.html) viser forskjellen mellom frossen base og finjustering.

Vi deler aldri treningsutvalget ved å hente nye eksempler fra det offisielle
testsettet. Kursrepoet inneholder nedlastingskode, ikke kopier av bildesamlingene
eller modellvektene. Ferdigtrente vekter har også en treningshistorie som må tas
med når man tolker sammenligninger.

## Attention og reinforcement learning

- [Vaswani mfl. Attention Is All You Need](https://arxiv.org/abs/1706.03762) introduserer transformerarkitekturen og scaled dot-product attention. Kursmodellen er en liten kausal modell, ikke en gjengivelse av hele originalens encoder–decoder.
- [Watkins og Dayan Q-learning](https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf) gir den klassiske tabellbaserte læringsregelen og betingelser for konvergens. Et endelig undervisningsforsøk er ikke en garanti om optimal policy.

Teksten i språkmodelløvelsen genereres av kurskoden som et kunstig meldingsspråk.
Rutenettet er et eget lite deterministisk miljø. Begge kan kjøres uten nedlasting.
