Build an interval timer and activity session manager full-stack application using FastAPI, Pydantic, SQLAlchemy, Svelte, SveleteKit.

Session is the main data model:
- Name
- Warmup/Presession Time
- Time between Series
- Rep Indicator: sound vs lights
- Series: n number of series per Session

Series data model:
- Activity
- Cadence (reps per minute)
- Set Time
- Rest After Set
- Number  of Sets

The frontend should show a countdown for the series timers, including the cadence timer which should result in rep indicator being triggered (sounds or lights). The interval should be visualized with a semi-circle countdown timer.


Create a SvelteKit frontend app in frontend dir that can visualize interval timer backend. The frontend should show a countdown for the series timers, including the cadence timer which should result in rep indicator being triggered (flashing background color change). The interval should be visualized with a semi-circle countdown timer. Add a Dockerfile and integrate into the docker-compose file in project root.

=====


Extra
Background Color
- labeling/customization generally
- 
Tags
- arbitrary tags on Series/Sessions
- e.g. weight
