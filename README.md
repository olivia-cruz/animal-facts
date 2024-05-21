<a name="readme-top"></a>

<br />
<div align="center">
  <a href="https://github.com/github_olivia-cruz/animal-facts">
    <img src="template/default.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Animal Fact Generator Microservice</h3>

  <p align="center">
    A Flask microservice that provides random animal facts.
    <!-- <br />
    <a href="https://github.com/github_olivia/repo_name"><strong>Explore the docs »</strong></a>
    <br /> -->
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <!-- <a href="https://github.com/github_username/repo_name/issues/new?labels=bug&template=bug-report---.md">Report Bug</a> -->
    <!-- ·
    <a href="https://github.com/github_username/repo_name/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a> -->
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
        <li><a href="#make-a-request">How to Make a Request</a></li>
        <li><a href="#receiving-data">Receiving your Data</a></li>
      </ul>
    </li>
      
    <li><a href="#receiving-data">Receiving your Data</a></li>
    <!-- <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This microservice provides random animal facts through a Flask API. It can be integrated into other websites to display fun and educational animal facts.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Flask][Flask]][Flask-url]
* [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

You need Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/github_olivia-cruz/animal-facts.git
   cd repo_name

### How to Make a Request

To request data from the Animal Fact Generator, use the following HTTP GET endpoints:
- `/facts` returns all animal facts.
- `/fact/random` returns a random fact.

Example call to fetch a random fact using curl:
```bash
curl http://localhost:5000/fact/random

### Receiving your Data
The data from the microservice is returned in JSON format. Here's how you can handle the JSON response in Python:
```python
import requests
response = requests.get('http://localhost:5000/fact/random')
data = response.json()
print(data)  # Prints the random animal fact received