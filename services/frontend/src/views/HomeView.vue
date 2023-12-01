<template>
  <CustomNavbar />
  <div
    class="relative w-full bg-cover bg-center bg-no-repeat"
    :style="{
      backgroundImage: 'url(' + homepageBackground + ')',
      minHeight: 'calc(100vh - 70px)',
    }"
  >
    <div
      class="absolute inset-0 bg-white bg-opacity-5 backdrop-blur z-10"
    ></div>
    <div class="container relative mx-auto pt-20 md:pt-32 z-20">
      <div class="items-center flex flex-wrap">
        <div class="w-full lg:w-10/12 px-4 ml-auto mr-auto text-center">
          <div class="pr-12">
            <h1 class="text-gray-700 font-semibold text-5xl">
              Tired of searching for Data Science resouces all over internet?
            </h1>
            <p class="mt-4 text-lg text-gray-500">
              Look no further! Dive into a vast ocean of knowledge with our
              curated selection. Discover an expansive library featuring over
              <b>5,000 books</b>, <b>1,500+ insightful videos</b>, and
              <b>250+ comprehensive courses</b>, all tailored to your Data
              Science learning needs. Your one-stop destination for top-tier
              Data Science resources is here.
            </p>
          </div>
        </div>
      </div>
    </div>
    <div class="w-11/12 relative mx-auto mt-20 md:mt-64 z-20">
      <div class="flex items-center justify-center">
        <label for="search" class="text-5xl font-semibold text-gray-700 mr-4">
          Give me resources for
        </label>
        <input
          id="search"
          ref="searchInput"
          v-model="searchQuery"
          type="text"
          placeholder="Enter search query"
          class="px-4 py-3 border-0 border-b-2 border-gray-700 outline-0 active:outline-none focus:outline-none placeholder-gray-400 text-3xl"
        />
      </div>
    </div>
  </div>
  <section class="pb-48">
    <div class="container mx-auto px-4 w-full">
      <div class="flex flex-wrap justify-center text-center mb-12">
        <div class="w-full lg:w-10/12 px-4">
          <h2 class="text-gray-700 font-semibold text-5xl">
            Our Data Partners
          </h2>
          <p class="mt-4 text-lg text-gray-500">
            We bring together a wide range of high-quality resources from
            trusted content platforms and data providers. Our goal is simple: to
            create an ever-growing, comprehensive list of the best data science
            materials available. Below are some of our valued data partners who
            play a key role in helping us achieve this mission.
          </p>
        </div>
      </div>
      <div class="flex flex-wrap">
        <div
          class="flex items-center justify-center w-full md:w-6/12 lg:w-2/12 lg:mb-0 mb-12 px-4"
        >
          <div class="flex items-center justify-center px-6">
            <img
              src="../assets/img/logo-google.svg"
              class="rounded-semi mx-auto max-w-250-px"
            />
          </div>
        </div>
        <div
          class="flex items-center justify-center w-full md:w-6/12 lg:w-2/12 lg:mb-0 mb-12 px-4"
        >
          <div class="flex items-center justify-center px-6">
            <img
              src="../assets/img/logo-open-library.svg"
              class="rounded-semi mx-auto max-w-250-px"
            />
          </div>
        </div>
        <div
          class="flex items-center justify-center w-full md:w-6/12 lg:w-2/12 lg:mb-0 mb-12 px-4"
        >
          <div class="flex items-center justify-center px-6">
            <img
              src="../assets/img/logo-youtube.svg"
              class="rounded-semi mx-auto max-w-250-px"
            />
          </div>
        </div>
        <div
          class="flex items-center justify-center w-full md:w-6/12 lg:w-2/12 lg:mb-0 mb-12 px-4"
        >
          <div class="flex items-center justify-center px-6">
            <img
              src="../assets/img/logo-amazon.svg"
              class="rounded-semi mx-auto max-w-250-px"
            />
          </div>
        </div>
        <div
          class="flex items-center justify-center w-full md:w-6/12 lg:w-2/12 lg:mb-0 mb-12 px-4"
        >
          <div class="flex items-center justify-center px-6">
            <img
              src="../assets/img/logo-udemy.svg"
              class="rounded-semi mx-auto max-w-250-px"
            />
          </div>
        </div>
        <div
          class="flex items-center justify-center w-full md:w-6/12 lg:w-2/12 lg:mb-0 mb-12 px-4"
        >
          <div class="flex items-center justify-center px-6">
            <img
              src="../assets/img/logo-coursera.svg"
              class="rounded-semi mx-auto max-w-250-px"
            />
          </div>
        </div>
      </div>
    </div>
  </section>
  <FooterSmall />
</template>

<script>
import homepageBackground from "@/assets/img/homepage_background.jpg";
import CustomNavbar from "@/components/Navbars/CustomNavbar.vue";
import FooterSmall from "@/components/Footers/FooterSmall.vue";
export default {
  data() {
    return {
      homepageBackground,
      searchQuery: "",
    };
  },
  mounted() {
    this.run();
  },
  components: {
    CustomNavbar,
    FooterSmall,
  },
  methods: {
    addToPlaceholder(toAdd, el) {
      const currentPlaceholder = el.getAttribute("placeholder") || "";
      el.setAttribute("placeholder", currentPlaceholder + toAdd);
      return new Promise((resolve) => setTimeout(resolve, 100));
    },
    clearPlaceholder(el) {
      el.setAttribute("placeholder", "");
    },
    printPhrase(phrase, el) {
      return new Promise((resolve) => {
        this.clearPlaceholder(el);
        let letters = phrase.split("");
        letters.reduce(
          (promise, letter, index) =>
            promise.then(() => {
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
        "Machine Learning Interpretability",
        "Expert Systems",
        "Natural Language Generation",
        "Blockchain Scalability Solutions",
        "Peer-to-Peer Lending Platforms",
        "Behavioral Email Targeting",
        "Immunotherapy in Cancer Treatment",
        "Marketing Analytics and ROI Measurement",
        "Wearable Health Technology",
        "Legal Chatbots and Virtual Assistants",
        "Predictive Analytics in Investment Banking",
        "Big Data in Actuarial Science",
        "Voice Search Optimization",
        "Medical Imaging Analysis with AI",
        "Cryptocurrency Market Analysis",
        "Compliance and Risk Management",
        "Cryptocurrency Analysis",
        "Voice Recognition Technologies",
        "Quantum Simulation",
        "Blockchain and IoT Integration",
        "Biostatistics",
        "Epigenomics Data Analysis",
        "Robotic Mapping and Localization",
        "Fuzzy Logic Systems",
        "Quantum Annealing",
        "Quantum Machine Learning",
        "Quantum Hardware and Qubits",
        "Quantum Networking",
        "Blockchain Governance",
        "Decentralized Finance (DeFi)",
        "Phylogenetic Analysis",
        "Systems Biology",
        "Drug Discovery and Design",
        "AI Ethics and Policy",
        "Molecular Dynamics Simulations",
        "Quantum Key Distribution",
        "Quantum Entanglement",
        "Drone Navigation Systems",
        "Computational Evolutionary Biology",
        "Robotics in Surgery",
        "Humanoid Robot Design",
        "Personalized Medicine",
        "Space Robotics",
        "AI-powered Predictive Maintenance",
        "Gesture Recognition for Human-Robot Interaction",
        "Robotics Control Systems",
        "Biological Network Analysis",
        "Swarm Intelligence",
        "Human-Robot Interaction",
        "Privacy and Anonymity in Cryptocurrencies",
        "Bioinformatics Algorithms",
        "Quantum Logic Gates",
        "Quantum Internet",
        "Genomic Data Analysis",
        "Underwater Robotics",
        "Evolutionary Computation",
        "Decentralized Autonomous Organizations (DAOs)",
        "Quantum Error Correction",
        "Emotion AI",
        "Quantum Algorithms",
        "Topological Quantum Computing",
        "Knowledge Representation",
        "Blockchain in Supply Chain Management",
        "Topic Modelling",
        "Recommender Systems",
        "Cybersecurity",
        "Graph Neural Networks",
        "Quantum Cryptography",
        "Soft Robotics",
        "Consensus Algorithms",
        "Token Economy and Mechanism Design",
        "Reinforcement Learning",
        "Metagenomics",
        "Quantum Supremacy and Complexity",
        "Blockchain Forensics",
        "Robotic Process Automation (RPA)",
        "Computational Neuroscience",
        "Autonomous Vehicles",
        "Collaborative Robots (Cobots)",
        "AI Planning Strategies",
        "Quantum Programming Languages",
        "Smart Contracts",
        "Swarm Robotics",
        "Cross-Chain Technologies",
        "Sensor Fusion in Robotics",
        "Protein Structure Prediction",
        "Distributed Ledger Technology",
        "AI in Healthcare Diagnostics",
        "Machine Perception for Robots",
        "Non-Fungible Tokens (NFTs)",
        "Computer Vision",
        "Natural Language Processing",
        "Data Structures",
        "Real-time Analytics in Financial Markets",
        "E-Discovery and Digital Litigation Support",
        "Augmented Reality in Retail",
        "Health Data Privacy and Security",
        "Financial Fraud Detection Techniques",
        "Forensic Science and Legal Evidence",
        "Stem Cell and Regenerative Medicine",
        "Precision Medicine and Personalized Treatment",
        "Personalized Marketing with AI",
        "Chatbots for Customer Service",
        "Robo-Advisors for Personal Finance",
        "Sustainable and Green Finance",
        "Programmatic Advertising Optimization",
        "Legal Document Automation",
        "Legal Predictive Analytics",
        "Video Marketing and Analytics",
        "Human Rights Law and Technology",
        "Financial Data Compliance and Governance",
        "Nanotechnology in Drug Delivery",
        "Predictive Sales Forecasting",
        "Antibiotic Resistance Mechanisms",
        "Computational Epidemiology",
        "Omnichannel Marketing Strategies",
        "Credit Scoring using Machine Learning",
        "Social Media Trend Analysis",
        "SEO and Content Marketing Automation",
        "Digital Health and Mobile Healthcare Applications",
        "Telemedicine and Remote Patient Monitoring",
        "Financial Risk Modeling",
        "Virtual Reality in Surgical Training",
        "Blockchain in Banking",
        "Genomic Sequencing in Diagnostics",
        "Cyber Law and Online Privacy Regulations",
        "Intellectual Property and Patent Analysis",
        "Customer Sentiment Analysis",
        "Algorithmic Trading Strategies",
        "Blockchain in Legal Record Keeping",
        "International Trade Law",
        "Influencer Marketing Effectiveness",
        "Environmental Law and Climate Change Policies",
        "InsurTech Innovations",
        "Alternative Dispute Resolution Mechanisms",
        "Neuroprosthetics and Brain-Computer Interfaces",
        "Electronic Health Records Optimization",
        "AI in Contract Review and Management",
        "Regulatory Technology (RegTech)",
        "Customer Lifetime Value Prediction",
        "Mobile Payment Security",
      ];

      this.printPhrases(phrases, this.$refs.searchInput);
    },
  },
};
</script>

<style></style>
