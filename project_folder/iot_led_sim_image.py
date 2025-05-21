{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "source": [
        "from flask import Flask, request, render_template_string,url_for\n",
        "app = Flask(__name__)\n",
        "# Biến mô phỏng trạng thái LED\n",
        "led_state = {\"value\": False}\n",
        "# HTML giao diện có hình ảnh LED\n",
        "HTML_TEMPLATE = \"\"\"\n",
        "<!DOCTYPE html>\n",
        "<html>\n",
        "<head>\n",
        "    <title>LED Control</title>\n",
        "</head>\n",
        "<body style=\"text-align:center; font-family:Arial\">\n",
        "    <h1>LED is currently: {{ state }}</h1>\n",
        "    <img src=\"{{ url_for('static', filename=image_file) }}\"\n",
        "width=\"120\"><br><br>\n",
        "    <a href=\"/?led=on\"><button style=\"padding:10px 20px;\">Turn\n",
        "ON</button></a>\n",
        "    <a href=\"/?led=off\"><button style=\"padding:10px 20px;\">Turn\n",
        "OFF</button></a>\n",
        "</body>\n",
        "</html>\n",
        "\"\"\"\n",
        "@app.route('/')\n",
        "def index():\n",
        "    led = request.args.get(\"led\")\n",
        "    if led == \"on\":\n",
        "        led_state[\"value\"] = True\n",
        "    elif led == \"off\":\n",
        "        led_state[\"value\"] = False\n",
        "    # Corrected indentation for the image_file assignment\n",
        "    image_file = \"led_on_white_120.png\" if led_state[\"value\"] else \"led_off_white_120.png\"\n",
        "    return render_template_string(\n",
        "        HTML_TEMPLATE,\n",
        "\n",
        "        state=\"ON\" if led_state[\"value\"] else \"OFF\",\n",
        "        image_file=image_file\n",
        "    )\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    app.run(host='0.0.0.0', port=5000)"
      ],
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2r2pTnw4w0Mt",
        "outputId": "5abf2b4e-4d26-43ac-c901-26bc1ed0282d"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " * Serving Flask app '__main__'\n",
            " * Debug mode: off\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "INFO:werkzeug:\u001b[31m\u001b[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\u001b[0m\n",
            " * Running on all addresses (0.0.0.0)\n",
            " * Running on http://127.0.0.1:5000\n",
            " * Running on http://172.28.0.12:5000\n",
            "INFO:werkzeug:\u001b[33mPress CTRL+C to quit\u001b[0m\n"
          ]
        }
      ]
    }
  ]
}