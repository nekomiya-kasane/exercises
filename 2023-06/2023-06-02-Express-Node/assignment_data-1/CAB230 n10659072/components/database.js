var knex = require("knex")

const db = knex({
	client: 'mysql',
	pool: {
		min: 2,
		max: 20,
	},
	connection: {
		host: '10.3.0.40', //process.env.DB_HOST,
		user: 'nekomiya', // process.env.DB_USERNAME,
		password: 'qhda2036', //process.env.DB_PASSWORD,
		database: 'test' //process.env.DB_DATABASE,
	},
});

module.exports = db