# Federation Manager

**Federation Manager** is an open-source Python component implementing the *Federation Management* functionality of the 
**Operator Platform (OP)**, as defined by the [GSMA Operator Platform Group (OPG)](https://www.gsma.com/solutions-and-impact/technologies/networks/gsma_resources/gsma-operator-platform-group-september-2024-publications/). 
This project aligns with the EWBI specifications outlined in the GSMA OPG document *"East-Westbound Interface APIs, (Version 4.0)"*.

## Description

The Federation Manager is responsible for enabling interconnection between multiple Operator Platforms deployed by 
different operators. It supports the discovery, negotiation, and management of federated services across administrative 
domains. By following GSMA standards, the Federation Manager ensures that operators can securely and efficiently offer, 
access, and consume services from each other's platforms.

## Motivation

As telecom operators move towards service-based, programmable networks, the need for a standardized inter-operator 
federation mechanism becomes critical. Federation Manager addresses this need by:

- Facilitating cross-operator service discovery and exposure.
- Enabling seamless negotiation and onboarding of federated services.
- Maintaining compatibility and interoperability based on GSMA’s Operator Platform specifications.

The Federation Manager is key to enabling operators to collaborate, extend coverage, and offer consistent service 
experiences across markets.

## What Does This Tool Do?

- **Lifecycle Management**: Control and monitor the resources and applications managed within the federation.
- **Federation Negotiation**: Support processes such as federation initiation, and termination.
- **Federated Service Discovery**: Allow operators to find services exposed by peer Operator Platforms.
- **Interoperability**: Communicate using standard APIs and protocols specified by the GSMA OPG.

## Features

- Standards-compliant federation workflows.
- Pluggable architecture to integrate with existing Operator Platform instances.
- RESTful API interfaces.
- Extensible to support future OPG federation evolutions.

## Compatibility

- Based on GSMA OPG Specifications: **OPG.02-v6.0** — *Operator Platform: Requirements and Architecture* and 
**OPG.04-v4.0** — *East-Westbound Interface APIs*.
- Designed to work with the Operator Platform core components and peer Federation Managers.

## Getting Started

_This section will include installation and usage instructions once the codebase is published._

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the [Apache 2.0 License](LICENSE).
