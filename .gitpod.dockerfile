FROM gitpod/workspace-base

RUN echo "CI version from base"

### Python Setup ###

USER gitpod

# Install required dependencies, but no need for distutils anymore
RUN sudo apt-get update && sudo apt-get install -y python3-pip

# Define persistent PYENV root inside /workspace
ENV PYENV_ROOT=/workspace/.pyenv
ENV PATH=$PYENV_ROOT/bin:$PYENV_ROOT/shims:$PATH

# Install pyenv and set the Python version persistently
ENV PYTHON_VERSION=3.12.0

RUN curl -fsSL https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash \
    && echo 'export PYENV_ROOT="/workspace/.pyenv"' >> ~/.bashrc \
    && echo 'export PATH="$PYENV_ROOT/bin:$PYENV_ROOT/shims:$PATH"' >> ~/.bashrc \
    && echo 'eval "$(pyenv init --path)"' >> ~/.bashrc \
    && pyenv update \
    && pyenv install $PYTHON_VERSION \
    && pyenv global $PYTHON_VERSION \
    && python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir --upgrade \
        setuptools wheel virtualenv pipenv rope flake8 \
        autopep8 pep8 pylama pydocstyle bandit notebook \
        twine \
    && sudo rm -rf /tmp/*

# Ensure Python persists across Gitpod restarts
RUN echo "$PYTHON_VERSION" > /workspace/.python-version

# Set up Python user base for persistent pip modules
ENV PYTHONUSERBASE=/workspace/.pip-modules \
    PIP_USER=yes
ENV PATH=$PYTHONUSERBASE/bin:$PATH

# Setup Heroku CLI
RUN curl https://cli-assets.heroku.com/install.sh | sh

# Add aliases
RUN echo 'alias heroku_config=". $GITPOD_REPO_ROOT/.vscode/heroku_config.sh"' >> ~/.bashrc && \
    echo 'alias python=python3' >> ~/.bashrc && \
    echo 'alias pip=pip3' >> ~/.bashrc && \
    echo 'alias arctictern="python3 $GITPOD_REPO_ROOT/.vscode/arctictern.py"' >> ~/.bashrc && \
    echo 'alias font_fix="python3 $GITPOD_REPO_ROOT/.vscode/font_fix.py"' >> ~/.bashrc && \
    echo 'alias make_url="python3 $GITPOD_REPO_ROOT/.vscode/make_url.py "' >> ~/.bashrc

# Local environment variables
ENV PORT=8080
ENV IP=0.0.0.0
