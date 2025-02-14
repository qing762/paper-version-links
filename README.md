> [!NOTE]  
> Join the [Discord server](https://qing762.is-a.dev/discord) for issues. Thanks a lot!

# Paper versions link

JSON containing links to the all known [PaperMC](https://papermc.io/) versions.

An API that is forked from [osipxd/Paper versions links](https://gist.github.com/osipxd/6119732e30059241c2192c4a8d2218d9) but it updates the JSON file with a script automatically.

## How it works

It fetches the versions & build numbers available from [PaperMC API](https://api.papermc.io) and format it into a JSON format, same as [osipxd's Paper versions links](https://gist.github.com/osipxd/6119732e30059241c2192c4a8d2218d9) .


## API Reference

### Get All PaperMC Versions

```http
GET https://qing762.is-a.dev/api/papermc
```

Returns the entire PaperMC versions data.

#### Response

```json
{
    "latest": "1.21.4",
    "versions": {
        "1.21.4": "https://api.papermc.io/v2/projects/paper/versions/1.21.4/builds/150/downloads/paper-1.21.4-150.jar",
        "1.21.3": "https://api.papermc.io/v2/projects/paper/versions/1.21.3/builds/82/downloads/paper-1.21.3-82.jar",
        ...
    }
}
```

### Get Latest PaperMC Version

```http
GET https://qing762.is-a.dev/api/papermc/latest
```

Returns the latest PaperMC version.

#### Response

```json
{
    "latest": "1.21.4",
    "url": "https://api.papermc.io/v2/projects/paper/versions/1.21.4/builds/150/downloads/paper-1.21.4-150.jar"
}
```

### Get Specific PaperMC Version Data

```http
GET https://qing762.is-a.dev/api/papermc/versions/{version}
```

Returns data for a specific PaperMC version.

#### Response

```json
{
    "version": "1.21.4",
    "url": "https://api.papermc.io/v2/projects/paper/versions/1.21.4/builds/150/downloads/paper-1.21.4-150.jar"
}
```

## Run Locally

To build the API yourself, follow the steps below:

Clone the project

```bash
git clone https://github.com/qing762/paper-version-links
```

Go to the project directory

```bash
cd paper-version-links
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the code 

```bash
python main.py
```

You should see a `paper-versions.json` file after this, meaning that it is built successfully and you can use the JSON file as an API for your projects.

## Contributing

Contributions are always welcome!

To contribute, fork this repository and improve it. After that, press the contribute button.

## Feedback / Issues

If you have any feedback or issues using the API, please join the [Discord server](https://qing762.is-a.dev/discord)

## License

[MIT LICENSE](https://choosealicense.com/licenses/mit/)