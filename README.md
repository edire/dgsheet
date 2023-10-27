# Description

A Python library by Dire Analytics for custom GSheet and Pandas communication.

## Installation

pip install git+https://github.com/edire/dgsheet.git

## Usage

```python
import dgsheet

df = dgsheet.read_gsheet(url='', filepath_cred=os.getenv('filepath_gcred'), skiprows=3)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT License

## Updates

10/27/2023 - Updated read_gsheet for traditional read_excel functionality.
06/26/2023 - Initial Commit.