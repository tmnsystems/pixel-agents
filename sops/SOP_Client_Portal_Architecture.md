# SOP: AI Product Delivery Portal Architecture (GoHighLevel)

**Purpose:**
This SOP outlines the exact architecture for delivering AI Software products (like CoachTinaMarieAI, VaultApp, etc.) securely to clients. It ensures that clients have a premium, self-service experience where they can log in, access downloads, get support, and manage their own subscriptions without requiring manual intervention from Tina.

**Platform:** GoHighLevel (GHL) + Stripe + Alethea (n8n/Knowledge Base)

---

## 1. User Login, Access, & Password Resets

We use the **GoHighLevel Client Portal** as the central secure hub.

- **Client Portal Setup:**
  - Navigate to **Memberships > Client Portal > Settings**.
  - Configure the branding (logo, dark mode colors).
  - Set the portal domain (e.g., `portal.tinamarie.com`).
- **Access Control:**
  - When a user purchases a product via a GHL/Stripe checkout (like the `universal-sales-page-coachtina.html` template), a GHL Workflow automatically grants them an "Offer".
  - Granting the Offer triggers the system to automatically email them login credentials.
- **Password Resets:**
  - **Zero-touch:** The GHL Client Portal natively includes a "Forgot Password" flow.
  - Users receive a "Magic Link" to securely reset their password or login with one click, eliminating the need for you to handle password reset tickets.

---

## 2. The "Download Area" & Product Delivery

To deliver the actual products (like custom prompts, HTML templates, or specialized knowledge bases), we use **GHL Courses/Memberships** embedded inside the Client Portal.

- **Structure:**
  - Create a new "Product" in GHL (e.g., _CoachTinaMarieAI Access_).
  - **Module 1: Getting Started** (Video instructions + Welcome text).
  - **Module 2: The Core App/Software** (This is where you can embed the custom HTML apps or link them out securely).
  - **Module 3: Download Vault** (Attach files, PDFs, or ZIP files directly to the lesson. GHL hosts these securely so only logged-in buyers can download them).

---

## 3. Self-Service Subscription Management

You want clients to be able to upgrade, downgrade, or cancel without messaging you.

- **Native Stripe Integration:**
  - Go to **Memberships > Client Portal > Settings**.
  - Ensure **"Manage Billing/Subscriptions"** is enabled in the App permissions.
  - **How it works:** When a logged-in user clicks on their profile, they will see a "Subscriptions" tab. Because GHL is directly integrated with your Stripe account, the user can natively view their invoices, update their credit card on file, or cancel their recurring `$97/mo` subscription directly from this portal.

---

## 4. 24/7 Support: Knowledge Base & AI Chat Widget

We do not want human support tickets blocking your time. We will embed an AI Chat Assistant into the portal.

- **The Chat Widget Front-End:**
  - Navigate to **Chat Widget** in GHL Settings.
  - Customize the widget to match the brand (Dark mode, Custom Avatar).
  - **Enable in Portal:** Go back to the Client Portal settings and toggle the Chat Widget to be visible inside the portal.
- **The AI Brain (Alethea/Dialogflow):**
  - **Data Source:** Compile an FAQ document for the specific product (e.g., "How do I reset my password?", "Where do I download the app?", "What is the 9 Fundamentals framework?").
  - Connect the GHL Chat Widget to Alethea via a webhook (n8n).
  - **Execution:** When a logged-in user types a question into the portal's chat widget, Alethea intercepts the message, checks the Knowledge Base, and responds instantly via the GHL API.
  - _(Note: Ensure text-only mode for this specific widget, disabling Voice to keep API costs down and focus on rapid support)._

---

## 5. Execution Sequence for a New Product

Whenever you launch a new product via the "Sell This" pipeline, follow this exact order:

1. **Create the Product:** In GHL Memberships, build the skeleton (Modules + Downloads).
2. **Create the Offer:** Price it and link it to Stripe.
3. **Build the Sales Page:** Use the `universal-sales-page-coachtina.html` template.
4. **Automate Access:** Build a GHL Workflow `[Trigger: Order Submitted] -> [Action: Grant Offer]`.
5. **Update Alethea's KB:** Feed the product's instruction manual to Alethea so she can answer support questions about it in the portal widget.
