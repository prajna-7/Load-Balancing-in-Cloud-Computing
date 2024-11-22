# 🌐 Load Balancing in Cloud Computing

Welcome! This repository demonstrates the implementation of a **Load Balancer** for HTTP requests in Microsoft Azure using virtualization techniques. 🚀 This project showcases the use of Python, Docker, and Flask to implement and test multiple load-balancing algorithms on virtual machines.

---

## **📚 Project Overview**

- **🎯 Objective**: Implement and demonstrate a load balancer using Azure Virtual Machines (VM4, VM5, VM6).
- **🛠 Tools Used**:
  - Azure Virtual Machines ☁️
  - Python 🐍 with Flask
  - Docker 🐳
- **💡 Key Features**:
  - ⚙️ Round Robin Load Balancing
  - 📊 Weighted Round Robin Load Balancing
  - 🧠 Workload-Sensitive Load Balancing
  - Lightweight, Dockerized setup for easy replication

---

## **📂 Project Structure**

```
Load-Balancing-in-Cloud-Computing/
├── VM4/                    # 🌐 Configuration files for VM4 (Web Server)
├── VM5/                    # 🌐 Configuration files for VM5 (Web Server)
├── VM6/                    # ⚙️ Configuration files for VM6 (Load Balancer)
├── Project_INFO_SDN.pdf    # 📄 Detailed project information
└── README.md               # 📝 Project documentation (you are here!)
```

---

## **🛠 Setup Instructions**

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Load-Balancing-in-Cloud-Computing.git
```

### 2️⃣ Configure Virtual Machines
- **🌐 VM4 and VM5**: Web servers configured with Flask to serve HTTP requests.
- **⚙️ VM6**: Load balancer using Flask with Round Robin, Weighted Round Robin, and Workload-Sensitive algorithms.

### 3️⃣ Dockerize the Setup 🐳
- Build Docker images for web servers and the load balancer.
- Run Docker containers using the commands provided in the `Dockerfile`.

Example:
```bash
docker build -t webserver-vm4 ./VM4
docker run -d --name webserver-vm4 -p 8080:8080 webserver-vm4
```

### 4️⃣ Test Load Balancing 🌐
Access the load balancer via its public IP or hostname to see requests distributed among the web servers.

---

## **🤖 Algorithms Implemented**

### 🔄 Round Robin
Sequentially distributes incoming requests to all available servers.

### ⚖️ Weighted Round Robin
Distributes requests based on predefined weights assigned to each server.

### 📈 Workload-Sensitive
Dynamically balances load based on real-time workloads of servers.

---

## **📊 Example Output**

1. **Round Robin Results**:
    ```
    VM4 -> VM5 -> VM4 -> VM5 ...
    ```

2. **Weighted Round Robin Results** (Weights: VM4=3, VM5=5):
    ```
    VM4, VM4, VM4, VM5, VM5, VM5, VM5, VM5 ...
    ```

3. **Workload-Sensitive Results**:
    Requests dynamically directed to the server with lower real-time workload.

---

## **📬 Contact**

For more information or questions, feel free to reach out:

📧 **Prajna Bala Sai Potnuri** - [prpo21@student.bth.se](mailto:prpo21@student.bth.se)  
📧 **Sri Phani Deverakonda** - [srdv21@student.bth.se](mailto:srdv21@student.bth.se)

