---
description: >-
  With the rise of Foundational Models, Vector Databases skyrocketed in
  popularity. Vector Database is also useful outside of a Large Language Model
  context.
---

# Vector Database

([Source](https://towardsdatascience.com/explaining-vector-databases-in-3-levels-of-difficulty-fc392e48ab78)) ([Source](https://www.linkedin.com/feed/update/urn:li:activity:7092611326891470849/))

The vector embedding takes a word or object and converts it into a bunch of numbers in a special way. This conversion is done in such a manner that similar words or objects end up having similar numbers in their embeddings. For instance, the embeddings of "cat" and "dog" would be close to each other because they share some similarities, both being animals. On the other hand, the embeddings of "cat" and "apple" would be far apart because they are very different things.

Vector embeddings help us understand relationships and similarities between different words or objects in a way that computers can easily handle and analyze. It's like giving words or objects a unique digital fingerprint, making them easier for computers to work with and compare. This concept is commonly used in natural language processing and various machine learning tasks.

The numerical representations enable us to apply mathematical calculations to objects, such as words, which are usually not suited for calculations. For example, the following calculation will not work unless you replace the words with their embeddings:

```
drink - food + hungry = thirsty
```

And because we are able to use the embeddings for calculations, we can also calculate the distances between a pair of embedded objects. The closer two embedded objects are to one another, the more similar they are.

### How does Vector Database work?

Vector databases are able to retrieve similar objects of a query quickly because they have already pre-calculated them. The underlying concept is called Approximate Nearest Neighbor (ANN) search, which uses different algorithms for indexing and calculating similarities.

As you can imagine, calculating the similarities between a query and every embedded object you have with a simple k-nearest neighbors (kNN) algorithm can become time-consuming when you have millions of embeddings. With ANN, you can trade in some accuracy in exchange for speed and retrieve the approximately most similar objects to a query.

**Indexing** — For this, a vector database **indexes** the vector embeddings. This step maps the vectors to a data structure that will enable faster searching. We will not go into the technical details of indexing algorithms, but if you are interested in further reading, you might want to start by looking up Hierarchical Navigable Small World (HNSW).

**Similarity Measures —** To find the nearest neighbors to the query from the indexed vectors, a vector database applies a similarity measure. Common similarity measures include cosine similarity, dot product, Euclidean distance, Manhattan distance, and Hamming distance.

### Database Operations

Let’s look into how one would interact with a Vector Database:

#### Writing/Updating Data

1. Choose a ML model to be used to generate Vector Embeddings.
2. Embed any type of information: text, images, audio, tabular. Choice of ML model used for embedding will depend on the type of data.
3. Get a Vector representation of your data by running it through the Embedding Model.
4. Store additional metadata together with the Vector Embedding. This data would later be used to pre-filter or post-filter ANN search results.
5. Vector DB indexes Vector Embedding and metadata separately. There are multiple methods that can be used for creating vector indexes, some of them: Random Projection, Product Quantization, Locality-sensitive Hashing.
6. Vector data is stored together with indexes for Vector Embeddings and metadata connected to the Embedded objects.

#### Reading Data

7. A query to be executed against a Vector Database will usually consist of two parts:

➡️ Data that will be used for ANN search. e.g. an image for which you want to find similar ones. ➡️ Metadata query to exclude Vectors that hold specific qualities known beforehand. E.g. given that you are looking for similar images of apartments - exclude apartments in a specific location.

8. You execute Metadata Query against the metadata index. It could be done before or after the ANN search procedure.
9. You embed the data into the Latent space with the same model that was used for writing the data to the Vector DB.
10. ANN search procedure is applied and a set of Vector embeddings are retrieved. Popular similarity measures for ANN search include: Cosine Similarity, Euclidean Distance, Dot Product.

Some popular Vector Databases: Qdrant, Pinecone, Weviate, Milvus, Faiss, Vespa.

<figure><img src="../.gitbook/assets/image (10).png" alt=""><figcaption><p>(<a href="https://www.linkedin.com/feed/update/urn:li:activity:7092611326891470849/">Source</a>)</p></figcaption></figure>
