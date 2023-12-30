# %% [markdown]
# # Test notebook

# %% [markdown]
# This notebook tests if these markdown images appear when the notebook file is viewed within github.
#
# #### Absolute link back to github using `https://github.com/hhoppe/test/raw/main/`
# <img src="https://github.com/hhoppe/test/raw/main/images/lake.png" width="120"/>
# <img src="https://github.com/hhoppe/test/raw/main/images/lake.png">
#
# #### Absolute link back to github using `https://raw.githubusercontent.com/hhoppe/test/main/`
# <img src="https://raw.githubusercontent.com/hhoppe/test/main/images/lake.png" width="120"/>
# <img src="https://raw.githubusercontent.com/hhoppe/test/main/images/lake.png">
#
# #### Local link
# <img src="images/lake.png" width="120"/>
# <img src="images/lake.png">
#
# #### Conclusions
#
# The result is that only images from local links are shown when the notebook is previewed on github.com
#
# When the notebook is opened as https://colab.research.google.com/github/hhoppe/test/blob/main/test.ipynb,
# the local images are copied.
# Therefore, local links seem best!
