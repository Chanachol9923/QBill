# QBill
A Python-based console application that simulates a restaurant queue and billing system.   It manages buffet package profiles, open/close table operations, customer queuing, and daily sales summaries — all through a command-line interface.

=====Features=====
- **Profile Setup**
  - Define number of buffet packages, prices, total tables, service charge, and VAT.
- **Table & Queue Management**
  - Open new bills for tables or queue customers when all tables are full.
  - Track real-time table status and queue list.
- **Billing System**
  - Auto-calculate totals with VAT and Service Charge.
  - Print simulated bills in console.
- **Summary Report**
  - Generate daily summary (`DD-MM-YY_Summary.txt`) including:
    - Total bills
    - Customer count
    - VAT, Service Charge
    - Net total revenue
- **Profile Editing**
  - Recreate or modify restaurant profile anytime.
  - 
=====Tech Stack=====
- **Language:** Python 3  
- **Libraries:** `os`, `sys`, `datetime`, `time` (standard library only)  
- **Storage:** Local text files (`Profile.txt`, `Summary.txt`)  
- **Interface:** Command-line (console)

=====How to Run=====
1. Make sure you have **Python 3** installed.  
2. Run the script:
   ```bash
   python QBill.py
