<!-- Favicon for Awesome List -->
[![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)

# Awesome Data Engineering Resources

A highly curated list of useful resources, repositories, blogs, and books for data engineering.

## 📑 Table of Contents
- [🤖 Agentic Coding](#-agentic-coding)
  - [📚 Repos](#-repos)
  - [🧠 Prompt Engineering & Memory Bank](#prompt-engineering--memory-bank)
- [📚 Books](#-books)
- [📰 Blogs](#-blogs)
- [🔄 Data Plattform Tools](#-data-plattform-tools)
- [🧱 Databricks](#-databricks)
  - [📚 Repos](#-repos-1)
  - [💡 Useful links & snippets](#-useful-links--snippets)
  - [📰 Blogs](#-blogs-1)
- [⚙️ DevOps & CI/CD](#-devops--cicd)
- [📑 Handbooks & Guides](#-handbooks--guides)
- [🔐 Data Privacy & Governance](#-data-privacy--governance)
- [📊 Reports](#-reports)
- [🧪 Testing](#-testing)
- [💡 Useful Code Snippets](#-useful-code-snippets)
- [💸 FinOps & Cost Management](#-finops--cost-management)

## 🤖 Agentic Coding
Agentic coding patterns, tools, and resources for building AI-driven and autonomous systems.

### 📚 Repos
Open-source repositories and frameworks for agentic coding and AI applications.
- [Dropped](https://github.com/pierceboggan/Dropped) - Open-source iOS project and resource for learning about agentic coding patterns.
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) - A 21-lesson course by Microsoft teaching the fundamentals of building Generative AI applications, including hands-on code samples in Python and TypeScript.
- [GitHub Copilot Vibe Coding Workshop](https://github.com/microsoft/github-copilot-vibe-coding-workshop/tree/main) - Self-paced workshop for building applications using GitHub Copilot Agent Mode, with multi-language samples and containerization.
- [Graphiti](https://github.com/getzep/graphiti) - Framework for building real-time, temporally-aware knowledge graphs for AI agents, supporting dynamic data integration and hybrid search.
- [MarkItDown](https://github.com/microsoft/markitdown) - Python tool for converting files and office documents to Markdown, designed for LLM and text analysis pipelines.

### 🧠 Prompt Engineering & Memory Bank
Guides and tools for prompt engineering and memory management in LLM and agentic workflows.
- [Cline Memory Bank Documentation](https://docs.cline.bot/prompting/cline-memory-bank#where-are-the-memory-bank-files-stored%3F) - Official documentation on where and how memory bank files are stored and managed in Cline.
- [OpenAI Cookbook: GPT-4 Prompting Guide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide) - Practical guide and examples for effective prompting with GPT-4, from the OpenAI Cookbook.

## 📚 Books
Recommended books on data engineering, architecture, and software best practices.
- [Building Medallion Architectures](https://www.oreilly.com/library/view/building-medallion-architectures/9781098178826/) - Comprehensive guide to building medallion data architectures.
- [Deciphering Data Architectures](https://www.oreilly.com/library/view/deciphering-data-architectures/9781098150754/) - Explains modern data architecture patterns and best practices.
- [Designing Data-Intensive Applications](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/) - In-depth exploration of data systems, scalability, and reliability.
- [Fundamentals of Data](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) - Essential concepts and principles for working with data.
- [The Pragmatic Programmer](https://www.oreilly.com/library/view/the-pragmatic-programmer/9780135956977/) - Classic book on software engineering best practices.
- [The Staff Engineers Path](https://www.oreilly.com/library/view/the-staff-engineers/9781098118723/) - Book on the role, responsibilities, and career path of staff engineers in modern software organizations.

## 📰 Blogs
Blogs and publications covering data engineering, analytics, and technology trends.
- [Confessions of a Data Guy](https://www.confessionsofadataguy.com/) - Blog on real-world data engineering.
- [Data Engineering Blog (Simon Spaethi)](https://www.ssp.sh/) - Technical blog by Simon Spaethi.
- [Data Engineering Weekly](https://www.dataengineeringweekly.com) - Weekly blog on data engineering trends and best practices.
- [DLT Hub Blog](https://dlthub.com/blog) - Blog for DLT Hub, covering data loading and transformation topics.
- [DuckDB Blog](https://duckdb.org/) - Official blog for DuckDB, an in-process SQL OLAP database management system.
- [dbt Developer Hub Blog](https://docs.getdbt.com/blog) - Blog for dbt (data build tool) developers, featuring updates, tutorials, and best practices.
- [Marvelous MLOps - Medium](https://medium.com/marvelous-mlops) - Medium publication focused on MLOps topics and best practices.
- [MotherDuck Blog](https://motherduck.com/blog/) - Blog for MotherDuck, a DuckDB-based analytics platform.
- [The GitHub Blog](https://github.blog/) - Official GitHub company blog.
- [Thoughtworks Insights](https://www.thoughtworks.com/insights) - Thoughtworks' insights and technology trends blog.
- [Visual Studio Code Blog](https://code.visualstudio.com/) - Official blog for Visual Studio Code, code editing, and development tips.
- [Overclocking dbt: Discord's Custom Solution in Processing Petabytes of Data](https://discord.com/blog/overclocking-dbt-discords-custom-solution-in-processing-petabytes-of-data) - Deep dive into how Discord scaled dbt to process petabytes of data, including custom solutions for multi-developer workflows, performance, and CI/CD guardrails.

## 🔄 Data Plattform Tools
Open-source tools and frameworks for building and managing data platforms.
- [Apache DataFusion Comet](https://github.com/apache/datafusion-comet) - Query acceleration for Apache DataFusion.
- [Apache Polaris](https://github.com/apache/polaris) - Snowflake Iceberg Catalog
- [astronomer/astronomer-cosmos](https://github.com/astronomer/astronomer-cosmos) - Tools and integrations for running dbt projects in Apache Airflow.
- [dbt-checkpoint](https://github.com/dbt-checkpoint/dbt-checkpoint) - Linting and checks for dbt projects.
- [dbt-coves](https://github.com/datacoves/dbt-coves) - Workflow automation for dbt projects.
- [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core) - Core dbt framework for analytics engineering.
- [dlt-hub/dlt](https://github.com/dlt-hub/dlt) - Data loading and transformation library for Python.
- [duckdb/dbt-duckdb](https://github.com/duckdb/dbt-duckdb) - dbt adapter for DuckDB, enabling analytics engineering workflows on DuckDB databases.
- [DuckLake](https://github.com/duckdb/ducklake) - Lakehouse implementation for DuckDB.
- [Koheesio](https://github.com/Nike-Inc/koheesio) - Orchestration framework for building data pipelines.
- [Lakehouse Engine](https://github.com/adidas/lakehouse-engine) - Lakehouse engine for scalable analytics by Adidas.
- [VSCode dbt Power User](https://github.com/AltimateAI/vscode-dbt-power-user/blob/master/package.json) - VSCode extension for enhanced dbt development.

## 🧱 Databricks
Resources, tools, and blogs for working with Databricks and the modern data stack.

### 📚 Repos
Official and community Databricks-related repositories and tools.
- [databricks/cli](https://github.com/databricks/cli) - Official Databricks CLI for automation and scripting.
- [databricks/databricks-vscode](https://github.com/databricks/databricks-vscode) - Visual Studio Code extension for Databricks development.
- [databricks/dbt-databricks](https://github.com/databricks/dbt-databricks) - dbt adapter for Databricks, enabling analytics engineering workflows on Databricks.
- [databrickslabs/discoverx](https://github.com/databrickslabs/discoverx) - Data discovery and cataloging tool for Databricks.
- [databrickslabs/dqx](https://github.com/databrickslabs/dqx) - Data quality framework for Databricks and Spark.
- [databricks/terraform-provider-databricks](https://github.com/databricks/terraform-provider-databricks) - Terraform provider for Databricks infrastructure automation.
- [Terraform Databricks SRA](https://github.com/databricks/terraform-databricks-sra) - Terraform modules and examples for implementing Databricks Security Reference Architecture.
- [UnityCatalog](https://github.com/unitycatalog/unitycatalog) - Open-source implementation of Unity Catalog for data governance.

### 💡 Useful links & snippets
Helpful links, code snippets, and resources for Databricks users.
- [DBSQL SME Resources](https://github.com/CodyAustinDavis/dbsql_sme/tree/main) - Resources and tools for Databricks SQL subject matter experts.
- [Databricks Playground](https://github.com/alexott/databricks-playground) - A collection of Databricks notebooks and resources for experimenting and learning.
- [Retrying dbt Runs in Databricks Workflows](https://community.databricks.com/t5/technical-blog/retrying-dbt-runs-in-databricks-workflows/ba-p/65766) - Databricks blog post on strategies for retrying dbt runs in workflows.

### 📰 Blogs
Blogs and publications focused on Databricks and its ecosystem.
- [Databricks AI - Medium](https://medium.com/@AI-on-Databricks) - Medium publication for AI topics on Databricks.
- [Databricks Blog](https://www.databricks.com) - Official Databricks company blog.
- [Databricks Community Blog](https://community.databricks.com/t5/technical-blog/bg-p/technical-blog) - Technical articles and updates from the Databricks community.
- [Databricks DBSQL SME - Medium](https://medium.com/dbsql-sme-engineering) - Medium publication for Databricks SQL SME engineering topics.
- [Databricks Platform SME - Medium](https://medium.com/databricks-platform-sme) - Medium publication for Databricks Platform subject matter experts.
- [Databricks SQL SME on Medium](https://medium.com/@databricks_sql_sme) - Medium publication for Databricks SQL SME.
- [Databricks UC SME - Medium](https://medium.com/databricks-unity-catalog-sme) - Medium publication focused on Databricks Unity Catalog subject matter expertise.

## ⚙️ DevOps & CI/CD
DevOps tools, CI/CD automation, and infrastructure resources for data engineering.
- [Commitizen CLI](https://github.com/commitizen/cz-cli) - Tool for creating conventional commit messages and automating releases.
- [Copier](https://github.com/copier-org/copier) - Project templating tool for generating and maintaining codebases.
- [Inspect Docker Images](https://github.com/pythonmonty/inspect-docker-images) - Tool for inspecting Docker images for vulnerabilities and metadata.
- [VSCode with Podman Desktop](https://podman-desktop.io/blog/2025/05/05/vs-code-with-podman-desktop) - Guide to integrating VSCode with Podman Desktop for container development.

## 📑 Handbooks & Guides
Comprehensive handbooks, guides, and documentation frameworks for data and engineering teams.
- [Diátaxis](https://diataxis.fr/) - Framework for organizing technical documentation by user needs, focusing on tutorials, how-to guides, reference, and explanation.
- [GitLab Enterprise Data Handbook](https://handbook.gitlab.com/handbook/enterprise-data/) - GitLab's official handbook for enterprise data management and governance.
- [Modern Data Engineering Playbook](https://www.thoughtworks.com/insights/e-books/modern-data-engineering-playbook) - Comprehensive guide on modern data engineering practices and principles.

## 🔐 Data Privacy & Governance
Resources and tools for data privacy, security, and synthetic data generation.
- [DataContract CLI](https://github.com/datacontract/datacontract-cli) - CLI tool for managing data contracts in data engineering workflows.
- [DataHub Project](https://github.com/datahub-project/datahub) - Metadata platform for the modern data stack.
- [Presidio](https://github.com/microsoft/presidio) - Open-source framework for detecting, redacting, masking, and anonymizing sensitive data (PII) in text, images, and structured data.
- [SDV: Synthetic Data Vault](https://github.com/sdv-dev/SDV) - Python library for generating synthetic tabular data using machine learning, with tools for evaluation, anonymization, and quality reporting.

## 📊 Reports
Industry reports, playbooks, and technology trend analyses for data engineering.
- [Looking Glass 2025](https://www.thoughtworks.com/en-de/insights/looking-glass) - Thoughtworks' long-term technology trend report exploring 90+ trends and their business impact, with strategic recommendations.

## 🧪 Testing
Testing tools, frameworks, and best practices for data and software engineering.
- [Inline Snapshot](https://github.com/15r10nk/inline-snapshot) - Tool for inline snapshot testing in Python.
- [Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) - Martin Fowler's article on the test pyramid and testing strategies.
- [Pytest Basics](https://github.com/The-Compiler/pytest-basics) - Examples and explanations for getting started with pytest.
- [Test Desiderata](https://testdesiderata.com/) - Philosophical and practical guidance for software testing.

## 💡 Useful Code Snippets
Handy code snippets and example repositories for data engineering tasks.
- [Building Medallion Architectures Book Repo](https://github.com/pietheinstrengholt/building-medallion-architectures-book) - The Repo to the book with useful code snippets.
- [The Hitchhiker's Guide to dbt](https://github.com/jeremyyeo/the-hitchhikers-guide-to-dbt) - A comprehensive guide and resource collection for working with dbt (data build tool).

## 💸 FinOps & Cost Management
Open-source tools and resources for cloud financial operations, cost management, and FinOps best practices.
- [FinOps Toolkit](https://github.com/microsoft/finops-toolkit) - Microsoft open-source toolkit for automating and extending FinOps capabilities in the Microsoft Cloud, including starter kits, automation scripts, and best practices.