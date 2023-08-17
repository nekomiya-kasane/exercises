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

db.schema.hasTable('users')
    .then(function (exists) {
        if (exists) {
            console.log("User table already exists.")
            return;
        } 
        const res = db.schema.createTable('users', function (table) {
            table.increments('id').primary();
            table.string('email').unique();
            table.string('password');
            table.string('firstName');
            table.string('lastName');
            table.date('dob');
            table.string('address');
        })
        console.log("User table created.")
        return res;
    }).then(function () {
        
    }).catch(function (err) {
        console.error(err)
    })

module.exports = db