# \# Azure Engineer Assignment

# 

# My submission for Symplique Solutions Azure Engineer assignment.

# 

# ---

# 

# \## ✅ Architecture Diagram

# 

# !\[Architecture Diagram](architecture.png)

# 

# ---

# 

# \## 📌 Solution Overview

# 

# \*\*Goal:\*\*  

# Reduce Cosmos DB cost by moving older billing records (> 3 months) to cheaper Blob Storage, while keeping them accessible via the same API.

# 

# \- \*\*Records 0–3 months old:\*\* Stored in Cosmos DB (fast access)

# \- \*\*Records older than 3 months:\*\* Moved to Blob Storage (low cost)

# \- \*\*API:\*\* If record not found in Cosmos DB → fallback to Blob Storage

# \- \*\*Archival:\*\* Automated with Azure Function running on a timer

# 

# ---

# 

# \## ⚙️ Implementation Highlights

# 

# \- \*\*Terraform file:\*\* `main.tf` (infra definition)

# \- \*\*Archival script:\*\* `archival\_function.py` (pseudocode for Azure Function)

# \- \*\*Diagram:\*\* `architecture.png` (this file)

# 

# ---

# 

# \## 📌 Key Benefits

# 

# ✅ Cost optimized  

# ✅ No data loss  

# ✅ No downtime  

# ✅ Same API contract

# 

# ---

# 



