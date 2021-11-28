
# DataStructure Journey
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

## Elementary Data Structures
In this section we are going to talk about simplest kind of data structures that we may face. But first we should know what a ***dynamic set*** is. A set in mathematics is a collection of data that  includes some unique data. However mathematical sets are unchanging, in computer science we define our own type of set that we call *dynamic set*. Every dynamic set has the ability to grow or shrink or change over time. A lot of data structures that we may introduce with in some point, is actually a dynamic set.

Every element of a dynamic set is a object with different attributes and one of these attributes is called the *key*. That's the attribute that we use when we want to compare two objects, or sort a dynamic set or ... . So in this sight we can say that if two objects evaluate equal in comparison, they're not really equal.

We can perform some operations on *dynamic sets*. Every operation is either a *query* or a *modifying operation*. A *query* simply returns information about the set and a *modifying operation* mutate the set.

 - `serch(S, k)`: This operation returns an element of *S* that its key value is *k* or `NIL` if there's no such element.
 - `insert(S, x)`: It's a modifying operation that adds element *x* to the set  *S*.
 - `delete(S, x)`: It's a modifying operation that removes element *x* from the subset *S*. It's not a query, so we don't need to look for the object *x* and we have the pointer of *x* instead of its *key* attribute's value.
- `minimum(S)`:  A query on a totally ordered set *S* that returns the element of *S* with the smallest key.
- `maximum(S)`:  A query on a totally ordered set *S* that returns the element of *S* with the largest key.
- `successor(S, x)`: A query on a totally ordered set *S* that gives element *x* and returns next larger element in *S*  according to the key attribute or it returns `NIL` if *x* is the maximum of the set *S*.
- `predecessor(S, x)`: A query on a totally ordered set *S* that gives element *x* and returns next smaller element in *S*  according to the key attribute or it returns `NIL` if *x* is the minimum of the set *S*.

## Variety

You can find more interesting information about each elementary data structure in following links:

 - [Stack](stack)
 - [Queue](queue)

