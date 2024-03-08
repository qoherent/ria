Qoherent welcomes code contributions from all participants who have signed a Contributor License Agreement (CLA). 
If you're interested in contributing to our codebase but haven't yet completed a CLA, please reach out to us at 
[info@qoherent.ai](mailto:info@qoherent.ai) for more details.

Not a coder? There are many other ways to get involved with the project. Please check out our 
[Contributing Guidelines](./CONTRIBUTING.md) for additional opportunities and information.


## Coding guidelines

To ensure smooth development, reduce frustration, and minimize conflicts, we kindly insist that all code 
contributions must adhere to these guidelines.

Think there's a better approach? We encourage challenges and discussions to continuously enhance and 
refine our approach. You're welcome to present your ideas and rationale on our [ideas forum](https://github.com/qoherent/michael/discussions/categories/ideas).

### General guidelines

RIA Core is a Python project. However, we occasionally integrate snippets of C where necessary to enhance performance.

Limit lines to 119 characters. This includes code, comments, docstrings.

All contributions must include appropriate unit tests and doctests. Please refer to our [testing guidelines](#testing-guidelines) 
for more information.

All contributions must be well documented, with ample inline comments and with a copious amount of complete 
docstrings. Please refer to our [documentation guidelines](#documentation-guidelines) for more information.

### Python-specific guidelines

We use [Flake8](https://flake8.pycqa.org/en/latest/) for code linting and style enforcement. All Python code must 
be formatted in accordance with the Flake8 configuration settings defined in the [tox.ini](../tox.ini) file 
in the root of the project.

To ensure a consistent development environment, this project uses [Poetry](https://python-poetry.org/) for dependency management. 
[Start here](https://python-poetry.org/docs/basic-usage/) for information on basic Poetry usage. Please refrain from making unnecessary updates to the 
`poetry.lock` file.

RIA Core is a typed project. Please include complete type annotations for all function parameters and return values. 

Prefer [keyword arguments](https://docs.python.org/3/glossary.html#term-argument?highlight=keyword%20argument) over positional arguments.

### C-specific guidelines

Coming soon: We are still developing our C-specific coding guidelines and the corresponding continuous integration (CI) 
tests. In the meantime, please format your C code in accordance with [Google's C/C++ Style Guide](https://google.github.io/styleguide/cppguide.html).

### Documentation guidelines

We use [Sphinx](https://www.sphinx-doc.org/en/master/) to auto-generate the project's [docs](http://docs.radiointelligence.io/). All docstrings must adhere to the 
[Sphinx docstring format](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html#the-sphinx-docstring-format).

Types mentioning in the docstring should be expressed in plain English rather than using Python's type hint syntax 
For example, write "int or float, optional" instead of "Optional[int | float]".

Please refer to [PEP-257](https://peps.python.org/pep-0257/) for further docstring conventions.

### Testing guidelines

We use [Pytest](https://docs.pytest.org/en/8.0.x/) to make our unit testing more efficient and expressive. To run our Pytest test suite:

1. [Activate a Poetry shell](https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment), ensuring that the `test` dependency group, which includes all the necessary dependencies for running tests, 
are installed.


2. Run tests with `poetry run pytest`.

Please include doctests as they provide clear and accessible examples of how to use RIA Core. 

### Guidelines for Git and GitHub

RIA Core development adheres to the standard [Git feature branch workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow). More information can be found in our 
section on [Our development process](#our-development-process).

Branch names should begin with the corresponding issue number. For instance, if you are addressing issue #7 
regarding README updates, your branch should be named as follows: "7-readme-updates".

Please avoid making changes to the commit history of open pull requests.

Please keep your commits [atomic](https://www.pauline-vos.nl/atomic-commits/). This makes your changes easier to understand and review.

Please keep your pull requests concise and focused. We recommend limiting your pull requests to around 300 lines.

## Building docs

We use [Sphinx](https://www.sphinx-doc.org/en/master/) to auto-generate the project's [docs](http://docs.radiointelligence.io/). When making changes, we use `sphinx-autobuild` to 
auto-detect these changes. This means you only need to build the docs once, and any changes to the source code or 
configurations are live-reload in the browser.

1. [Activate a Poetry shell](https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment), ensuring that the `docs` dependency group, which includes all the necessary 
dependencies for building the docs, are installed.


2. Navigate to the `docs` directory and execute:
```commandline
make clean
sphinx-autobuild ./source ./build/html
```


3. A working copy of the docs will now be available at http://localhost:8000/, and any changes made to the source 
code or configurations will be automatically reflected there.


**Important:** if you've added new modules, you may need to execute `sphinx-apidoc -o ./source ../ria` (from 
within the `docs` directory) and manually update the `index.rst` files to include links to any the new 
pages. More information on how we use sphinx-apidoc to auto-generate documentation from the docstrings can be 
found [here](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/build-the-docs.html#generating-documentation-from-docstrings).


## Our development process

Contributors develop on their own forked copy of the RIA Core project and propose changes to the upstream project 
through [pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests). 

Proposed changes must pass our suite of CI tests and be approved by an authorized Qoherent team member prior to being 
merged in to the upstream repository.

If you encounter any issues with our development process, please don't hesitate to [reach out for support](https://github.com/qoherent/ria/discussions/categories/support).

### Initial setup for first-time contributors
If you are a first-time contributor, please complete the following steps to initialize your development environment:

1. Please ensure you have reviewed our [Code of Conduct](./CODE_OF_CONDUCT.md), [Contributing Guidelines](./CONTRIBUTING.md), and the above
[Coding Guidelines](#coding-guidelines). Additionally, ensure you've reviewed and signed a Contributor License Agreement.


2. Ensure that [Python](https://www.python.org/downloads/), [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), and [Poetry](https://python-poetry.org/docs/) are installed on the computer you intend to use for 
development, and that you're logged into your account on [GitHub](https://github.com/).


3. Visit the [RIA Core](https://github.com/qoherent/ria) project on GitHub, and use the [Fork button](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository) to create your own copy of the project. 


4. Clone down your project fork to your local computer:
```commandline
git clone https://github.com/your-username/ria.git
```


5. Add RIA Core as an upstream repository:
```commandline
git remote add upstream https://github.com/qoherent/ria.git
```


6. Pull the latest changes from upstream:
```commandline
git pull upstream main
```


7. Initialize Poetry from the `pyproject.toml` file at the root of the project:
```commandline
poetry init
```

Give yourself a pat on the back - you're now set up and ready to begin development! 🎉


### Author your contribution

**Important:** First-time contributors should complete the prerequisite [setup instructions](#initial-setup-for-first-time-contributors) before starting 
development. Please do not begin development on any issues until the `needs triage 📥` label has been removed. This 
is to ensure your efforts are focused effectively. We appreciate your patience and understanding.

1. Pull the latest changes from upstream and ensure that your Poetry environment is up-to-date. This is important
to ensure you are working off the latest version of the project and to minimize merge conflicts, as well as to 
maintain a consistent development environment with other contributors.
```commandline
git pull upstream main
poetry update
```


2. Create a new local feature branch. It is important to choose a meaningful branch name since it will
appear in the merge message. Keep in mind that branch names should start with the corresponding issue number.
```commandline
git checkout -b \#-my-feature-branch
```


3. Develop your contribution on your local feature branch, committing regularly as you progress. Don't forget to 
include tests for and document your code. 


4. Ensure all unit tests are passing:
```commandline
poetry run pytest
```


4. Confirm your changes are formatted in accordance with our Flake8 style configuration:
```commandline
flake8 .
```


5. Ensure that docstrings are properly formatted in the [Sphinx docstring format](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html#the-sphinx-docstring-format) and that the Sphinx 
documentation, which is generated from these docstrings in a semi-automatic manner, looks okay. Please refer 
to [Building docs](#building-docs) for more information on building, inspecting, and updating the project's docs. 


5. Once you have completed development, all tests are passing, and there are no Flake8 errors or warnings, push 
your changes to your project fork on GitHub. This will require you to [authenticate with GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github).


### Submit your contribution for review

1. Ensure your changes align with our [Coding Guidelines](#coding-guidelines).


2. If your change introduces a deprecation, we ask that you discuss this on the [discussion forum](https://github.com/qoherent/ria/discussions/categories/general) prior
to submitting a pull request.


3. Submit your pull request: 
   1. Navigate to your fork on GitHub: [https://github.com/your-username/ria.git]().
   2. Your new feature branch will show up with a green Pull Request button.
   3. Fill out our pull request template honestly and to the best of your abilities, ensuring that you check 
   all checkboxes. ☑️


4. Your pull request will trigger a suite of CI tests to build and test the code on your branch, as well as to 
check for code coverage and style issues. If any of these CI tests fail, you will need to make changes. 


5. Once your proposed changes pass our suite of automated tests, they will be reviewed by an authorized member of 
the Qoherent development team, who will provide inline and/or general feedback. If your pull request hasn't been 
reviewed within a week, please ping us on the [discussion forum](https://github.com/qoherent/ria/discussions/categories/general) to ensure it hasn't slipped through the cracks.


6. Once your changes have been approved by an authorized Qoherent team member, we will merge them into the 
upstream repository. You receive an automated notification from GitHub once your pull request has been merged, at 
which time the branch containing your changes can then be safely deleted.


7. If your contribution introduces a new feature or significantly alters functionality, we kindly ask that you post 
on the [discussion forum](https://github.com/qoherent/ria/discussions/categories/general) to explain your changes. This is especially important if your changes introduce any 
user-facing modifications we need to mention in the release notes.


A heartfelt thank you from everyone at Qoherent and the broader radio community for taking the time to contribute 
to RIA Core. We understand that you're busy and deeply appreciate your time and expertise in helping us in our mission 
to drive the creation of intelligent radios! 🙏💖
