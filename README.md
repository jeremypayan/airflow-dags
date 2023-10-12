# Airflow Repository
Repository dedicated to airflow dags management. For testing, we use a Cloud Composer instance. 



# Airflow Architecture

Cloud Composer is a **fully managed workflow orchestration service built on the Apache Airflow** open-source project. It is designed to allow developers, data scientists, and other users to easily create, schedule, and monitor data pipelines in the cloud.

The architecture of Cloud Composer consists of several components that work together to provide a scalable and reliable workflow orchestration service:

1. **Airflow**: At the heart of Cloud Composer is the Apache Airflow open-source project, which provides the core workflow orchestration functionality. Airflow allows users to define, schedule, and monitor complex workflows using a Python-based DSL.

2. **Cloud Storage**: Cloud Composer uses Google Cloud Storage as its primary storage backend. All code, data, and metadata for workflows are stored in Cloud Storage buckets. 

3. **Cloud SQL**: Cloud Composer also uses Google Cloud SQL as its backend database for storing Airflow's metadata. Cloud SQL provides a fully managed, scalable, and reliable relational database service.

4. **Kubernetes**: Cloud Composer uses Kubernetes as its underlying container orchestration system to manage the Airflow scheduler, workers, and other components. Kubernetes provides a scalable and flexible infrastructure for running and managing containers in the cloud. 

5. **Google Cloud APIs**: Cloud Composer also relies on several Google Cloud APIs, including the Compute Engine API for creating and managing VMs, the Cloud IAM API for managing access control, and the Cloud Logging API for monitoring and logging.


This infrastructure is provided with Terraform : cf. [Repository](https://github.com/jeremypayan/terraform-cloud-composer). We use Cloud Composer' s Environment 2 and we use Airflow under version 2.4.3. 


# Code Architecture 

The architecture is very basic : 

- **dags** (directory) : Add your amazing dags here ! 
- requirements.txt : Airflow dependencies (2.4.3)
- constraints.txt : dags dependencies
- requirements-test.txt : dependencies for running tests

All the stuff is under dags directory. 

# CI/CD stuff

Here is the final process I target : 
1. You make a change to a DAG and push that change to a dev branch in your repository
2. You open a pull request against the dev branch of your repository
3. Github Actions runs unit tests to check your DAG is valid (CI) 
and syncs your Dag with our development environment (CD) 
4. Your pull request is approved and merged to your dev branch and you verify that the DAG behaves as expected in your development environment
5. You open a pull request against the main branch of your repository (at least one approval)
6. Github Actions runs unit tests to check your DAG is valid (CI) 
5. Github Actions syncs your Dag with our prod environment (CD) 

At this moment we skip 3. and 4. steps. 

## Continuous Integration

We run automated DAG unit tests thanks to pytest and airflow unit test utilities. The Continuous integration is under *test-dags.cloudbuild.yaml* file. 

Here is some documentation: 
- [cloud-composer-dag-test-utils](https://pypi.org/project/cloud-composer-dag-test-utils/)
- [airflow unit tests](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#unit-tests)

Basically we chek if the Dag is going to be upload correctly on the UI. 

## Continuous Deployment 

We Synchronize DAGs in our Cloud Composer environment with DAGs. To do that we sync the GCS bucket corresponding to our DAG bag.


The Continuous Deployment is under *sync_dag_bucket.yml* file. 


# To get started 

1. Clone the repository:
    - HTTPS: `git clone https://github.com/jeremypayan/airflow-dags.git`
    - SSH: `git clone git@github.com:jeremypayan/airflow-dags.git`


2. Create a conda environment : `$> conda create -y airflow`.

3. Activate your new conda environment : `$> conda activate airflow`

4. Install airflow dependencies: `$> pip install -r requirements.txt` and python requirements : `$> pip install -r constraints.txt`



