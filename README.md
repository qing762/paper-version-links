> [!NOTE]  
> Join the [Discord server](https://qing762.is-a.dev/discord) for issues. Thanks a lot!

> [!WARNING]
> Please be advised that usage of this tool is entirely at your own risk. I assumes no responsibility for any adverse consequences that may arise from its use, and users are encouraged to exercise caution and exercise their own judgment in utilizing this tool.

# Paper versions link

An API that is forked from [osipxd/Paper versions links](https://gist.github.com/osipxd/6119732e30059241c2192c4a8d2218d9) but it update the json file with a script automatically.

## How it works

It fetch the version & build number from [PaperMC API](https://api.papermc.io) and format it into a JSON format, same as [osipxd's Paper versions links](https://gist.github.com/osipxd/6119732e30059241c2192c4a8d2218d9) .


## API Reference

```http
  GET https://qing762.is-a.dev/api/papermc
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

You should see a `paper-versions.json` file after this, meaning that it is built successfully and you can use the json file as an API for your projects.



## Contributing

Contributions are always welcome!

To contribute, fork this repository and improve it. After that, press the contribute button.

## Feedback / Issues

If you have any feedback or issues using the API, please join the [Discord server](https://qing762.is-a.dev/discord)


## License

[MIT LICENSE](https://choosealicense.com/licenses/mit/)


