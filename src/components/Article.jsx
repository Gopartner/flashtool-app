import React from 'react';
import articleData from '../data/artikel.json';

const Article = () => {
  return (
    <article className="p-4">
      <h2 className="text-lg font-bold">{articleData.title}</h2>
      <p className="mt-2">{articleData.content}</p>
    </article>
  );
}

export default Article;

