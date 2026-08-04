import modal

app = modal.App("example-import-torch")


torch_image = modal.Image.debian_slim().uv_pip_install(
    "torch",
    extra_index_url="https://download.pytorch.org/whl/cu128",
    force_build=True,  # trigger a build every time, just for demonstration purposes
    # remove if you're using this in production!
)


@app.function(gpu="T4", image=torch_image)
def torch() -> list[list[int]]:
    import math

    import torch

    print(torch.cuda.get_device_properties("cuda:0"))

    matrix = torch.randn(1024, 1024) / math.sqrt(1024)
    matrix = matrix @ matrix

    return matrix.detach().cpu().tolist()


@app.local_entrypoint()
def main():
    print(torch.remote()[:1])
