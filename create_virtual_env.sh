python -m venv /workspace/myenv
source /workspace/myenv/bin/activate
pip install uv
uv pip install ipykernel
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"