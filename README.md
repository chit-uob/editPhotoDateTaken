# Script to edit the date taken attribute of photos based on their file name, and place them in respective folders

## Background

I have some photos lying around without the dateTaken attribute, therefore the photo organiser cannot organize them.

I wish to write this script to add the dateTaken attribute manually, so the photos can be organized.

such as: Screenshot_20201115-134117_YouTube.jpg

I would set the date taken as 2020-11-15

Then I would add them to the respective folder.

## Challenges

Different images have different naming formats, some may have a prefix, suffix, infix.

The date string may have different format as well, it may be ddmmyyyy, or yyyymmdd.

So I have to identify which format are they using, and validate that they make sense

## Plan

I plan to first save the source and destination folder.

Then I would define some regex (maybe not actually regex) to match for the filenames.

Then I would scan the source folder matching the regex, adding the predicted date as a suffix, and put them in a temp folder.

Validate the temp folder, if they are correct, actually make the change and put them in the correct folder.

