import React, { useEffect, useState } from 'react';
import './App.css';
import Posts from './components/posts';
import PostLoadingComponent from './components/postLoading';
import axiosInstance from 'axios';

function App() {
  const PostLoading = PostLoadingComponent(Posts);
	const [appState, setAppState] = useState({
		loading: true,
		posts: null,
	});
	const [error, setError] = useState(null);

	useEffect(() => {
		const apiURL = 'http://127.0.0.1:8000/api/'
		axiosInstance.get(apiURL)
		.then((res) => {
			const allPosts = res.data;
			setAppState({ loading: false, posts: allPosts });
		})
		.catch(err => {
			setAppState({ loading: false,});
			setError(err.message);
		});
	}, [setAppState]);
	return (
		<div className="App">
			<h1>Latest Posts</h1>
			<PostLoading isLoading={appState.loading} posts={appState.posts} />
			<h1>{error}</h1>
		</div>
	);
}

export default App;
