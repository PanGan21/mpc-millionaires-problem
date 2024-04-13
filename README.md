# mpc-millionaires-problem

Building an implementation of garbled circuits from scratch

## Background

### Multi-Party Computation (MPC) and Privacy:

Multi-Party Computation (MPC) is a cryptographic technique that enables multiple parties to jointly compute a function over their private inputs without revealing those inputs to each other. It allows for secure collaboration where each participant can maintain the privacy of their sensitive data while still achieving a collectively desired outcome. MPC ensures that no individual party can learn any more information than what is revealed by the output of the computation.

MPC is instrumental in preserving privacy in various scenarios, such as secure auctions, financial transactions, and data analysis, where sensitive information must be kept confidential while still allowing for collaborative analysis or decision-making.

Reference: [Secure Multi Party Computation](https://en.wikipedia.org/wiki/Secure_multi-party_computation)

### Garbled Circuits

Garbled Circuits are a cryptographic technique used in MPC protocols to securely evaluate functions while preserving the privacy of the inputs. In a garbled circuit, the function to be evaluated is represented as a circuit, and each gate in the circuit is "garbled" with encrypted information corresponding to the possible inputs and outputs of the gate. By exchanging and evaluating these garbled gates, parties can securely compute the function's output without revealing their inputs.

Garbled circuits provide a powerful tool for implementing MPC protocols, enabling secure computation of arbitrary functions while maintaining privacy.

Reference: [Yao's Garbled Circuit](https://en.wikipedia.org/wiki/Garbled_circuit)

### The Millionaires' Problem

The Millionaires' problem is a classic example used to illustrate the concept of MPC. It involves two millionaires, each knowing only their respective wealth and wishing to determine who is richer without revealing their exact wealth to each other.

In the context of MPC, the Millionaires' problem is a simple yet powerful demonstration of how parties can securely compare private inputs without disclosing sensitive information. By employing MPC techniques such as Garbled Circuits, the millionaires can jointly compute the function for comparing their wealth while keeping their individual net worths private.

Reference: [Millionaires problem](https://en.wikipedia.org/wiki/Yao%27s_Millionaires%27_problem#:~:text=The%20problem%20discusses%20two%20millionaires,without%20revealing%20their%20actual%20wealth.&text=The%20Millionaires'%20problem%20is%20an,e%2Dcommerce%20and%20data%20mining.)

### POC

This implementation is a Proof Of Concept of a toy implementation. Therefore **DON'T USE IN PRODUCTION**.

### WIP

This POC is still work in progress
