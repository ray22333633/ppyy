{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "104_Crawler.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/gist/LinYenCheng/c480e235d83dcfa54b30e07a3a0a92c3/104_crawler.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 623
        },
        "id": "yylTLH-Ndr41",
        "outputId": "86332bf8-669a-4f0c-a6a6-58212b4958b1"
      },
      "source": [
        "!pip install selenium\n",
        "!apt-get update # to update ubuntu to correctly run apt install\n",
        "!apt install chromium-chromedriver\n",
        "!cp /usr/lib/chromium-browser/chromedriver /usr/bin\n",
        "import sys\n",
        "sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')\n",
        "from selenium import webdriver\n",
        "import pandas as pd\n",
        "chrome_options = webdriver.ChromeOptions()\n",
        "chrome_options.add_argument('--headless')\n",
        "chrome_options.add_argument('--no-sandbox')\n",
        "chrome_options.add_argument('--disable-dev-shm-usage')\n",
        "browser = webdriver.Chrome('chromedriver',chrome_options=chrome_options)\n",
        "\n",
        "url = 'https://www.esunbank.com.tw/bank/about/announcement/announcement?i=eqQb451_o06vZeJpBZLLLQ'\n",
        "\n",
        "browser.get(url)\n",
        "# pd.read_html(browser.page_source)[0].head()\n",
        "\n",
        "element_xpath = '//*[@id=\"mainform\"]/div[10]/div[2]/div[2]/table[1]'\n",
        "target_table = browser.find_element_by_xpath(element_xpath)\n",
        "html_string = target_table.get_attribute('outerHTML')\n",
        "pd.read_html(html_string)[0].head()\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: selenium in /usr/local/lib/python3.7/dist-packages (3.141.0)\n",
            "Requirement already satisfied: urllib3 in /usr/local/lib/python3.7/dist-packages (from selenium) (1.24.3)\n",
            "Hit:1 http://security.ubuntu.com/ubuntu bionic-security InRelease\n",
            "Ign:2 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  InRelease\n",
            "Hit:3 https://cloud.r-project.org/bin/linux/ubuntu bionic-cran40/ InRelease\n",
            "Ign:4 https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  InRelease\n",
            "Hit:5 http://ppa.launchpad.net/c2d4u.team/c2d4u4.0+/ubuntu bionic InRelease\n",
            "Hit:6 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64  Release\n",
            "Hit:7 https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64  Release\n",
            "Hit:8 http://archive.ubuntu.com/ubuntu bionic InRelease\n",
            "Hit:9 http://ppa.launchpad.net/cran/libgit2/ubuntu bionic InRelease\n",
            "Hit:10 http://archive.ubuntu.com/ubuntu bionic-updates InRelease\n",
            "Hit:11 http://archive.ubuntu.com/ubuntu bionic-backports InRelease\n",
            "Hit:12 http://ppa.launchpad.net/deadsnakes/ppa/ubuntu bionic InRelease\n",
            "Hit:13 http://ppa.launchpad.net/graphics-drivers/ppa/ubuntu bionic InRelease\n",
            "Reading package lists... Done\n",
            "Reading package lists... Done\n",
            "Building dependency tree       \n",
            "Reading state information... Done\n",
            "chromium-chromedriver is already the newest version (93.0.4577.63-0ubuntu0.18.04.1).\n",
            "0 upgraded, 0 newly installed, 0 to remove and 37 not upgraded.\n",
            "cp: '/usr/lib/chromium-browser/chromedriver' and '/usr/bin/chromedriver' are the same file\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:13: DeprecationWarning: use options instead of chrome_options\n",
            "  del sys.path[0]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>0</th>\n",
              "      <th>1</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>項目</td>\n",
              "      <td>2021年8月</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1.流通卡數</td>\n",
              "      <td>6534077</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2.有效卡數</td>\n",
              "      <td>4460909</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>3.當月發卡數</td>\n",
              "      <td>45847</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>4.當月停卡數</td>\n",
              "      <td>22348</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
              ],