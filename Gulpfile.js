'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var cssMinify = require('gulp-minify-css');

const PATHS = {
	CSS: './static/css'
};

gulp.task('css', function() {
	gulp.src('sass/**/*.scss')
		.pipe(sass().on('error', sass.logError))
		.pipe(cssMinify({compatibility: 'ie8', processImport: false}))
		.pipe(gulp.dest(PATHS.CSS));
});

gulp.task('build', ['css']);

gulp.task('default', function() {
	gulp.watch('sass/**/*.scss', ['css']);
});