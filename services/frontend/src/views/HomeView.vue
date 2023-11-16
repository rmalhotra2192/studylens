<template>
  <div class="flex items-center justify-center h-screen">
    <div class="flex items-center justify-center">
      <label for="search" class="text-5xl font-medium text-gray-700 mr-4">
        Give me resources for
      </label>
      <input
        id="search"
        ref="searchInput"
        v-model="searchQuery"
        type="text"
        placeholder="Enter search query"
        class="px-4 py-3 border-0 border-b-2 border-gray-700 outline-0 active:outline-0 focus:outline-0 placeholder-gray-400 text-4xl"
      />
    </div>
  </div>
</template>

<script>
export default {
  data() {
      return {
        searchQuery: '',
      };
  },
  mounted() {
      this.run();
  },
  methods: {
    addToPlaceholder(toAdd, el) {
        const currentPlaceholder = el.getAttribute("placeholder") || '';
        el.setAttribute("placeholder", currentPlaceholder + toAdd);
        return new Promise((resolve) => setTimeout(resolve, 100));
    },
    clearPlaceholder(el) {
      el.setAttribute("placeholder", "");
    },
    printPhrase(phrase, el) {
        return new Promise(resolve => {
            this.clearPlaceholder(el);
            let letters = phrase.split('');
            letters.reduce(
                (promise, letter, index) => promise.then(() => {
                    if (index === letters.length - 1) {
                        setTimeout(resolve, 1000);
                    }
                    return this.addToPlaceholder(letter, el);
                }),
                Promise.resolve()
            );
        });
    },
    printPhrases(phrases, el) {
        phrases.reduce(
            (promise, phrase) => promise.then(() => this.printPhrase(phrase, el)), 
            Promise.resolve()
        );
    },
    run() {
        let phrases = [
            "Deep Learning",
            'Machine Learning Interpretability',
            'Expert Systems',
            'Natural Language Generation',
            'Blockchain Scalability Solutions',
            'Peer-to-Peer Lending Platforms',
            'Behavioral Email Targeting',
            'Immunotherapy in Cancer Treatment',
            'Marketing Analytics and ROI Measurement',
            'Wearable Health Technology',
            'Legal Chatbots and Virtual Assistants',
            'Predictive Analytics in Investment Banking',
            'Big Data in Actuarial Science',
            'Voice Search Optimization',
            'Medical Imaging Analysis with AI',
            'Cryptocurrency Market Analysis',
            'Compliance and Risk Management',
            'Cryptocurrency Analysis',
            'Voice Recognition Technologies',
            'Quantum Simulation',
            'Blockchain and IoT Integration',
            'Biostatistics',
            'Epigenomics Data Analysis',
            'Robotic Mapping and Localization',
            'Fuzzy Logic Systems',
            'Quantum Annealing',
            'Quantum Machine Learning',
            'Quantum Hardware and Qubits',
            'Quantum Networking',
            'Blockchain Governance',
            'Decentralized Finance (DeFi)',
            'Phylogenetic Analysis',
            'Systems Biology',
            'Drug Discovery and Design',
            'AI Ethics and Policy',
            'Molecular Dynamics Simulations',
            'Quantum Key Distribution',
            'Quantum Entanglement',
            'Drone Navigation Systems',
            'Computational Evolutionary Biology',
            'Robotics in Surgery',
            'Humanoid Robot Design',
            'Personalized Medicine',
            'Space Robotics',
            'AI-powered Predictive Maintenance',
            'Gesture Recognition for Human-Robot Interaction',
            'Robotics Control Systems',
            'Biological Network Analysis',
            'Swarm Intelligence',
            'Human-Robot Interaction',
            'Privacy and Anonymity in Cryptocurrencies',
            'Bioinformatics Algorithms',
            'Quantum Logic Gates',
            'Quantum Internet',
            'Genomic Data Analysis',
            'Underwater Robotics',
            'Evolutionary Computation',
            'Decentralized Autonomous Organizations (DAOs)',
            'Quantum Error Correction',
            'Emotion AI',
            'Quantum Algorithms',
            'Topological Quantum Computing',
            'Knowledge Representation',
            'Blockchain in Supply Chain Management',
            "Topic Modelling",
            "Recommender Systems",
            "Cybersecurity",
            "Graph Neural Networks",
            'Quantum Cryptography',
            'Soft Robotics',
            'Consensus Algorithms',
            'Token Economy and Mechanism Design',
            'Reinforcement Learning',
            'Metagenomics',
            'Quantum Supremacy and Complexity',
            'Blockchain Forensics',
            'Robotic Process Automation (RPA)',
            'Computational Neuroscience',
            'Autonomous Vehicles',
            'Collaborative Robots (Cobots)',
            'AI Planning Strategies',
            'Quantum Programming Languages',
            'Smart Contracts',
            'Swarm Robotics',
            'Cross-Chain Technologies',
            'Sensor Fusion in Robotics',
            'Protein Structure Prediction',
            'Distributed Ledger Technology',
            'AI in Healthcare Diagnostics',
            'Machine Perception for Robots',
            'Non-Fungible Tokens (NFTs)',
            "Computer Vision",
            "Natural Language Processing",
            "Data Structures",
            'Real-time Analytics in Financial Markets',
            'E-Discovery and Digital Litigation Support',
            'Augmented Reality in Retail',
            'Health Data Privacy and Security',
            'Financial Fraud Detection Techniques',
            'Forensic Science and Legal Evidence',
            'Stem Cell and Regenerative Medicine',
            'Precision Medicine and Personalized Treatment',
            'Personalized Marketing with AI',
            'Chatbots for Customer Service',
            'Robo-Advisors for Personal Finance',
            'Sustainable and Green Finance',
            'Programmatic Advertising Optimization',
            'Legal Document Automation',
            'Legal Predictive Analytics',
            'Video Marketing and Analytics',
            'Human Rights Law and Technology',
            'Financial Data Compliance and Governance',
            'Nanotechnology in Drug Delivery',
            'Predictive Sales Forecasting',
            'Antibiotic Resistance Mechanisms',
            'Computational Epidemiology',
            'Omnichannel Marketing Strategies',
            'Credit Scoring using Machine Learning',
            'Social Media Trend Analysis',
            'SEO and Content Marketing Automation',
            'Digital Health and Mobile Healthcare Applications',
            'Telemedicine and Remote Patient Monitoring',
            'Financial Risk Modeling',
            'Virtual Reality in Surgical Training',
            'Blockchain in Banking',
            'Genomic Sequencing in Diagnostics',
            'Cyber Law and Online Privacy Regulations',
            'Intellectual Property and Patent Analysis',
            'Customer Sentiment Analysis',
            'Algorithmic Trading Strategies',
            'Blockchain in Legal Record Keeping',
            'International Trade Law',
            'Influencer Marketing Effectiveness',
            'Environmental Law and Climate Change Policies',
            'InsurTech Innovations',
            'Alternative Dispute Resolution Mechanisms',
            'Neuroprosthetics and Brain-Computer Interfaces',
            'Electronic Health Records Optimization',
            'AI in Contract Review and Management',
            'Regulatory Technology (RegTech)',
            'Customer Lifetime Value Prediction',
            'Mobile Payment Security'
        ];

        this.printPhrases(phrases, this.$refs.searchInput);
    }
  },
};
</script>

<style>
</style>