# graph-data-tools

# GitHub App Token Generator

This Python script interacts with the GitHub API to generate a JSON Web Token (JWT) for authentication and retrieve an installation access token for a GitHub App. It also provides functionality to list issues from a specified GitHub repository.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.x installed on your machine.
- The following Python packages installed:
  - `python-jwt`
  - `requests`
  - `python-dotenv`

You can install the required packages using pip:

bash
pip install python-jwt requests python-dotenv


## Environment Variables

Create a `.env` file in the same directory as the script and add the following variables:

plaintext
GITHUB_APP_ID=your_github_app_id
GITHUB_PRIVATE_KEY_PATH=path_to_your_private_key.pem
GITHUB_INSTALLATION_ID=your_installation_id


- `GITHUB_APP_ID`: The ID of your GitHub App.
- `GITHUB_PRIVATE_KEY_PATH`: The path to your GitHub App's private key file (in PEM format).
- `GITHUB_INSTALLATION_ID`: The installation ID of your GitHub App.

## Usage

To run the script, execute the following command in your terminal:

bash
python git_app.py


The script will list the issues from the specified GitHub repository. You can modify the `list_issues` function call in the `if __name__ == "__main__":` block to specify your GitHub username and repository name:


list_issues("your_github_username", "your_repository")


## Functions

- `generate_jwt()`: Generates a JWT for GitHub App authentication.
- `get_installation_token()`: Retrieves an installation access token using the generated JWT.
- `list_issues(owner, repo)`: Lists issues from the specified GitHub repository.

## Troubleshooting

If you encounter issues, ensure that:

- The environment variables are correctly set in the `.env` file.
- The GitHub App is installed on the repository you are trying to access.
- The private key file is accessible and correctly specified.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Instructions

1 Open your terminal.
2 Navigate to the directory where you want to create the README file:

   cd /Users/stephen/Git/graph-data-tools/

3 Open or create the README.md file in a text editor of your choice and paste the above content into it.
4 Save the file.
