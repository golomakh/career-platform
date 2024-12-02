# Personalized Development Plan - Career Platform

## Overview

This project is a user-friendly platform that helps individuals receive personalized development plans tailored to their skills and goals. The platform allows users to track their progress, get AI-driven recommendations, and access curated learning resources to improve their skills and career prospects.

Additionally, the platform integrates with various online learning platforms through APIs to provide users with real-time access to relevant courses, articles, and tutorials. Based on the user’s goals, skill level, and test results, the system offers AI-driven course recommendations, ensuring the learning path is efficient and tailored to the user's needs. These recommendations dynamically adjust as the user progresses, helping them stay on track and continuously improve their expertise in specific areas.

## Features

- **Admin Panel for Content Management**: An easy-to-use Django admin panel has been set up to manage users, topics, test results, and development plans. This allows administrators to quickly add, modify, and delete topics or adjust the user data without direct database access.
- **Personalized Development Plans**: (in process). Automatically generated learning paths based on user inputs and test results, including topics to learn, priority levels, estimated time to complete, and progress tracking.
- **Topic Management**: (in process). A database of learning topics is created, with categories based on skill level. Each topic includes a title, description, priority, and estimated duration, giving users a structured view of the learning content.
- **Scalable Architecture**: (in process). Built with Django, enabling future integrations and flexibility for new features such as team collaboration tools or company-level development plans. The platform is built using Django, with future plans for scaling via microservices. 
- **Microservices Architecture**: (in process). The platform is designed with a microservices architecture to ensure scalability and flexibility. Different services (e.g., user management, recommendations, course integrations) operate independently, allowing easy updates and maintenance without affecting the entire system.
- **AI-Powered Recommendations**: (future). AI-driven suggestions for courses, books, and articles tailored to the user's needs. Integration with external learning platforms for up-to-date resources. The goal is to integrate Google Cloud's PaLM 2 / Vertex AI Natural Language to generate course suggestions based on user data and goals.
- **Test and Feedback System**: (future). Short quizzes to assess the user's knowledge and determine areas of improvement, with personalized feedback and further learning suggestions.
- **API Integration**: (future). External Learning Platforms will be integrated via APIs to dynamically fetch up-to-date courses, articles, and other study materials. This will allow the platform to offer a vast and continuously updated selection of learning resources, ensuring users always have access to the latest and most relevant content for their personal development journey.



## Tools & Technologies


- **Core Architecture: Microservices with Django**:  

  - **Microservices Architecture**: The platform is structured with a microservices approach, dividing functionality into independent services that can be scaled, updated, and deployed separately. This allows for easier maintenance and flexibility as the platform grows.

  - **Django**: The main framework for backend development. Each microservice is implemented as a separate Django app handling different functionalities such as user management, courses, recommendations, and analytics.

  - **Django REST Framework (DRF)**: DRF allows for easy creation of RESTful APIs, making data exchange between microservices efficient and straightforward. This will facilitate integration with future AI and external learning APIs.




- **Backend Development (Server-side)**:  

  - **Django**: Framework used to build a scalable and robust backend.

  - **Django REST Framework (DRF)**: Used for creating APIs that allow for communication between microservices, ensuring scalability and flexibility in future system enhancements.

  - **gRPC (Future)**:Planned for future use to optimize communication between microservices, ensuring low-latency, high-speed data exchange.

  - **Docker & Kubernetes**: Each microservice will be containerized using Docker, allowing for consistent development and deployment environments. Kubernetes will manage the orchestration of these containers, ensuring automatic scaling and system reliability.



- **Databases & Storage**:  

  - **SQLite**: (now). Database used for local development and testing.

  - **PostgreSQL**: (future). PostgreSQL will be used for relational data storage, handling user data, courses, and development plans with scalability and integration capabilities.

  - **Google Cloud Storage**: For storing large files such as videos or study materials, ensuring reliability and scalability.



  
- **Virtual Environment**:  
  - **venv**: To isolate project dependencies and avoid conflicts.



- **API Integration**: Integration with online learning platforms for fetching up-to-date resources.



- **AI Integration & Analytics**:   

  - **Google Cloud AI Integration (Future)**: Plans to integrate PaLM 2 / Vertex AI Natural Language for generating personalized course recommendations based on user data and learning goals. This will help deliver smarter, data-driven learning paths.

  - **TensorFlow (Future)**: For building advanced machine learning models to enhance course recommendations and personalized learning pathways.

  - **Scikit-learn (Future)**: For initial recommendation systems, Scikit-learn provides quick and easy-to-set-up models, ideal for prototyping the platform’s AI-powered features.

  




- **Infrastructure & Deployment**: 

  - **Docker & Kubernetes**: Docker will be used for containerizing microservices, while Kubernetes will manage and scale these containers across cloud infrastructure, ensuring optimal performance.

  - **CI/CD (GitHub Actions or GitLab CI)**: GitHub Actions or GitLab CI will be used to automate testing, deployment, and ensure continuous delivery for rapid updates and stability.

  - **Google Cloud Platform (GCP)**:  For cloud infrastructure, with GCP being the preferred choice due to its integration with AI tools. The free tiers of GCP  are ideal for initial development, while scaling will be easier with these platforms.


- **Testing Tools**:  
  - **pytest**: Used for testing backend functionality and the accuracy of generated development plans.


- **File Processing**:  
  - **CSV/JSON Libraries**: For exporting and importing data, such as learning plans and test results.



- **Security & Compliance**: 

  - **Auth0 or Firebase Authentication**: For handling secure authentication and authorization, ensuring GDPR compliance and integrating with OAuth2 for a seamless login experience.

  - **SSL Certification & API Protection**: Ensures secure communication between microservices, using SSL encryption to maintain data integrity and privacy in line with GDPR requirements.



- **Monitoring & Analytics**:  

  - **Prometheus**: Used for monitoring system performance and visualizing the health of microservices, providing a clear overview of the platform’s operations.

- **Google Analytics**: For tracking user activity and generating insights into how users interact with the platform, helping optimize features and user engagement.






## Installation

To get the project up and running locally, follow these steps:

1. **Clone the repository**:

   First, clone the repository to your local machine using Git:

   ```bash
   git clone https://github.com/golomakh/career-platform.git
   cd career-platform

