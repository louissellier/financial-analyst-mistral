<p align="center">
  <img src="logo-mistral.png" alt="Mistral Logo" width="200"/>
</p>

# ⚡️ Lightweight AI-Powered Financial Analyst with Multi-Agent Workflow

📺 **See a live demo:**  
A walkthrough of this tool is available on my [LinkedIn post](https://www.linkedin.com/feed/update/urn:li:activity:7351572546833588224/)

---

This project builds a streamlined financial analysis assistant capable of parsing stock market data and delivering actionable insights.

Built on a multi-agent architecture powered by **CrewAI**, the system coordinates roles and responsibilities between agents to generate robust financial reports. Instead of relying on heavy, costly models, it leverages **Mistral Small** and **NeMo** to deliver fast, efficient performance at a fraction of the cost.

The result: a low-latency, high-impact financial analysis pipeline that’s local-first, modular, and production-ready.

---

## 🧠 What It Does

Once set up, the assistant allows users to query real-time or historical stock data and receive structured outputs—charts, summaries, and comparisons—all orchestrated through a backend agentic workflow. The architecture is designed to be extensible, allowing seamless integration of new models, tools, or data sources.

Whether you're comparing company performance, analyzing trends, or investigating market behavior, this assistant simplifies complex workflows into a smooth interactive experience.

---

## 💬 Example Prompts

- "Compare Meta and Amazon’s stock trends over the last year"
- "Plot Tesla's stock performance from 2022-01-15 to 2024-07-11"

**Advanced Example:**

> "Implement the following portfolio with weights:  
> AAPL: 30%, MSFT: 25%, NVDA: 20%, GOOGL: 15%, AMZN: 10%  
> Compare it against the S&P 500 index (^GSPC) from 2022-01-01 to 2025-07-16.  
> Output a cumulative return chart (portfolio vs. benchmark), and include portfolio statistics on the graph."

This kind of prompt triggers multi-agent collaboration to fetch, align, and visualize financial data while embedding key performance metrics—delivering analysis that would otherwise require manual coding and domain knowledge.

---

## 🤝 Contributing

Open to all contributions—bug fixes, new features, or enhancements to the agent roles. Fork the repo and submit a pull request anytime.
