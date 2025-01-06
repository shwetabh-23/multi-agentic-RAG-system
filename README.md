# Multi-Agentic RAG Systems for Jamming Sessions

This repository presents a research-oriented project that combines Multi-Agent Systems, Retrieval-Augmented Generation (RAG), and Large Language Models (LLMs) for dynamic song recommendations. The system leverages LangChain for orchestrating the RAG pipeline, Chroma for vector database integration, and Meta's Llama2 for multi-agentic decision-making to create an engaging, personalized jamming experience.

# Overview

Music recommendation systems are a cornerstone of modern entertainment applications, providing tailored playlists and suggestions to users. This project takes the concept further by introducing a multi-agentic framework for recommending songs dynamically during a jamming session. The agents work collaboratively to analyze song features, recommend appropriate tracks, and validate recommendations based on the session's context.

# The primary technologies used include:

## LangChain: 
A framework for building multi-agentic RAG systems.

## Chroma: 
A high-performance vector database for storing and querying song embeddings.

## 
Llama2 (7B-chat-hf): A powerful open-source language model used for inference.

# System Architecture

The project implements a three-agent system:

## 1. Song Analysis Agent

This agent analyzes the initial song's characteristics (e.g., tempo, energy, danceability) and queries the vector database to fetch similar songs.

## 2. Song Recommendation Agent

Given the context of the current song and the options retrieved by the Song Analysis Agent, this agent uses Llama2 to recommend the most suitable next song for the jamming session.

## 3. Validation and Feedback Agent

This agent validates the recommended song against the session's context, user preferences, and history. If the recommendation is unsuitable, it suggests an alternative.

# Features

## Dynamic Recommendation Loop:
The system runs in a continuous loop, dynamically analyzing, recommending, and validating songs.

## Context Awareness: 
Maintains a session history to avoid repetitive or unsuitable recommendations.

## Modular Design: 
Agents are implemented as independent modules for flexibility and scalability.

# Workflow

Initialize the session with an initial song.

Song Analysis Agent fetches similar songs based on characteristics.

Song Recommendation Agent suggests the next song.

Validation and Feedback Agent ensures the recommendation aligns with the session context.

Repeat for subsequent songs, maintaining a session history.

# Future Work

## Enhance Embeddings: 
Experiment with advanced embeddings for richer song representations.

## Additional Agents: 
Introduce agents for mood detection and genre exploration.

## Cross-Platform Integration: 
Adapt the system for real-time use in music streaming services.

# Contributing

Contributions are welcome! Please open an issue or submit a pull request for any suggestions or improvements.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgments

Meta AI for open-sourcing Llama2.

LangChain for the RAG framework.

Chroma for the vector database.