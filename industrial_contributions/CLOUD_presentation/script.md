🗣️ Slide 1 – Title Slide

Good morning everyone, and thank you for attending this session.
I’m Julien Soulé, a PhD candidate at Université Grenoble Alpes and Thales LAS. Today, I’ll present our work titled “Streamlining Resilient Kubernetes Autoscaling with Multi-Agent Systems”, developed jointly with my colleagues from LCIS and AICA.
This work is part of our broader effort to bring intelligent automation and resilience to cloud infrastructures, particularly Kubernetes.

🗣️ Slide 2 – Context and Problem

Kubernetes clusters are widely adopted but remain fragile under dynamic or adversarial conditions, such as DDoS attacks, resource contention, or pod crashes.
Traditional autoscalers like the Horizontal Pod Autoscaler are reactive and typically based on threshold rules, which makes them ineffective against complex, multi-dimensional failures.
RL-based autoscalers improve adaptation but tend to optimize single metrics like latency, ignoring other crucial dimensions like integrity or availability.
What we need is an autoscaling system that handles multiple types of failures collaboratively, by integrating distributed intelligence.

🗣️ Slide 3 – Related Works

Many approaches have emerged in this space.
RL-based systems like Gym-HPA or QoS-RL work well in simulation but lack support for multi-agent reasoning or explainability.
AWARE introduces adversarial robustness, but it remains mono-agent.
Hybrid approaches like AHPA, KOSMOS, and COPA are more rule-based and reactive, with limited learning capacity.
Overall, existing solutions rarely support multi-agent coordination, explainability, or structured reasoning—this is the gap we aim to fill.

🗣️ Slide 4 – Our Proposition: KARMA

To address these challenges, we propose KARMA: a 4-phase framework that integrates organizational principles into MARL for resilient autoscaling.
KARMA decomposes autoscaling into specialized roles and missions. It uses MARL agents guided by constraints to learn coordinated behavior.
The system operates in closed loop: we model the environment, train agents in simulation, analyze their behaviors, and deploy them to the real cluster.
This is not just a learning approach—it’s a structured online MAS design loop.

🗣️ Slide 5 – Phase 1: Modeling (Digital Twin)

In the first phase, we collect execution traces from the real cluster.
We use these to build a digital twin—modeled as a zero-sum stochastic game between defenders and a virtual attacker.
A neural network approximates unknown transitions, allowing us to simulate the environment realistically.
This lets us train policies safely, with near-realism, without disturbing production services.

🗣️ Slide 6 – Phase 2: Training

In phase two, we train agents using MAPPO—Multi-Agent Proximal Policy Optimization.
Each agent is assigned a role with its own Role Action Guide (RAG) that restricts its action space.
Missions are defined via Goal Reward Guides (GRG), which shape rewards or enforce hard constraints.
These guides come from the MOISE+MARL framework we introduced at AAMAS 2025.
They allow the system to structure learning, ensuring agents specialize while remaining coordinated.

🗣️ Slide 7 – Phase 3: Analyzing Agent Behaviors

Once training is done, we analyze the learned behaviors.
Using clustering over trajectories, we infer implicit roles and goals from agent actions and observations.
This provides post-hoc explainability and helps validate that agents behave according to the organizational design.
This phase is based on the TEMM method, which helps quantify organizational fit.

🗣️ Slide 8 – Phase 4: Transfer

In the final phase, we transfer trained policies to the real Kubernetes cluster.
Agents interact with the cluster through the Kubernetes API to make scaling decisions.
A fallback mechanism is implemented to ensure safety during execution.
Meanwhile, the digital twin stays updated with live metrics, enabling continuous adaptation and retraining if needed.

🗣️ Slide 9 – Experimental Setup

We evaluated KARMA on a simulated Kubernetes environment consisting of 4 services deployed in a pipeline: A to D.
Each service has different configurations, capacities, and potential failure points.
We inject adversarial events like DDoS attacks, pod crashes, or resource exhaustion.
Training and evaluation were run on a high-performance GPU cluster.

🗣️ Slide 10 – Comparative Evaluation (1/2)

Here, we compare KARMA against leading baselines such as AWARE, Rlad-core, and Gym-HPA.
KARMA achieves the highest success rate at 90.9%, the best latency compliance, and the lowest number of pending requests.
It also recovers faster from DDoS attacks and maintains the highest availability.
This shows that our design enables better operational resilience and adversarial robustness.

🗣️ Slide 11 – Comparative Evaluation (2/2)

The learning curves show that KARMA converges faster and more consistently.
Organizational constraints reduce the policy search space and accelerate learning.
Moreover, the multi-agent structure enables better generalization across different failure types.
This is key for real-world deployment, where workloads are unpredictable.

🗣️ Slide 12 – Explainability & Organizational Fit

Thanks to the analysis phase, we can verify how closely learned behaviors align with the intended organizational design.
For instance, by clustering action sequences, we identify roles such as DDoS Manager or Resource Manager.
We also compute metrics like structural and functional fit to measure how well agents fulfill their intended missions.
This enhances explainability and supports both debugging and refinement.

🗣️ Slide 13 – Ablation Studies

We performed ablation studies to assess the importance of each component.
Removing the digital twin reduced performance by 11%.
Switching to a mono-agent architecture led to higher latency and worse coordination.
Removing organizational constraints slowed convergence and increased variance.
In short, each component matters—the full stack delivers the best trade-off between performance, safety, and explainability.

🗣️ Slide 14 – Conclusion & Perspectives

To conclude, KARMA addresses key gaps in Kubernetes autoscaling:
It enables online multi-agent system design, incorporates organizational constraints, and supports explainability and safe deployment.
Our next steps include testing on real Kubernetes clusters with multiple nodes, extending to streaming services, and exploring the use of LLMs to document agent behaviors.
Thank you for your attention, and I’ll be happy to take your questions.