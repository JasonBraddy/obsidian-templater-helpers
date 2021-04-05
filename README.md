# obsidian-templater-helpers

These are scripts intended to be used with the [Templater](https://github.com/SilentVoid13/Templater) plugin for [Obsidian](https://obsidian.md).

`obs_dates_nav.py`, when invoked via macro expansion by Templater in a new Daily Note, should do two things:
  - Add a navigation link to the most recent previous Daily Note
  - Go the most recent previous Daily Note and update its forward link to the current day's note

(While Templater already has macro expansions for `{{yesterday}}` and `{{tomorrow}}`, using these to create navigation links assumes that you create a Daily Note every single day. If that works for you it's definitely simpler than this solution, but I happen to enjoy weekends and holidays.)

`obs_todo_migr.py`, when invoked via macro expansion by Templater in a new Daily Note, in intended to migrate uncompleted Todo items (denoted by the `- [ ]` pattern) from the most recent previous Daily Note to the new one. It will also append a string of your choice to the end of each Todo item every time it is migrated to make it easier to identify things that are being carried over day after day, as this is an indication that the item is either not really a priority or perhaps needs to be refactored into smaller chunks to progress.

To be usable these scripts need to be edited to reflect the actual location of your Daily Notes folder, and need to be linked to custom macro expansions (see below) in Templater which are in turn used in your Daily Note template file (an example called `Daily Template.md` is included). Note that if you're installing Templater for the first time it's wise to restart Obsidian afterwards, as there seems to be a bug with plugin initialization that causes macros to not expand on file creation after Templater is first installed.

<img width="735" alt="Screen Shot 2021-04-05 at 2 02 11 PM" src="https://user-images.githubusercontent.com/7127258/113614098-a9ac7d00-9617-11eb-903b-92da53cf4bb1.png">

These were tested on Python 3.7.5 on MacOS with Obsidian v0.11.9 and Templater 0.5.7, and are provided as is as examples of what is possible with Templater and simple scripts. Since these do make changes to your notes files, backups are probably a good idea.
