# Python I2C Driver for Sensirion LPS22

This repository contains the Python driver to communicate with a Sensirion LPS22 sensor over I2C.

<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-lps22/master/images/product-image-st-lps22.jpeg"
    width="300px" alt="LPS22 picture">


Click [here](https://www.st.com/en/mems-and-sensors/lps22hb.html) to learn more about the Sensirion LPS22 sensor.


For details about the command please consult the datasheet https://www.st.com/resource/en/datasheet/lps22hb.pdf



The default I²C address of [LPS22](https://www.st.com/en/mems-and-sensors/lps22hb.html) is **0x5c**.



## Connect the sensor

You can connect your sensor over a [SEK-SensorBridge](https://developer.sensirion.com/product-support/sek-sensorbridge/).
For special setups you find the sensor pinout in the section below.

<details><summary>Sensor pinout</summary>
<p>
<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-lps22/master/images/product-pinout.jpeg"
     width="300px" alt="sensor wiring picture">

| *Pin* | *Cable Color* | *Name* | *Description*  | *Comments* |
|-------|---------------|:------:|----------------|------------|
| 1 |  | NC | Do not connect |


</p>
</details>


## Documentation & Quickstart

See the [documentation page](https://sensirion.github.io/python-i2c-lps22) for an API description and a
[quickstart](https://sensirion.github.io/python-i2c-lps22/quickstart.html) example.


## Contributing

In case you want to contribute to this project, please read the [contribution guidelines]((https://sensirion.github.io/python-i2c-lps22/contributing.html)).

## License

See [LICENSE](LICENSE).