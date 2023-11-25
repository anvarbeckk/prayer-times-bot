from aiogram import types


async def set_default_commands(dp):
    await dp.bot.delete_my_commands()
    # await dp.bot.set_my_commands(
    #     [
    #         types.BotCommand(command="start", description="about info"),
    #         types.BotCommand(command="help", description="how to use the bot"),
    #         types.BotCommand(command="prayer_times", description="seeing prayer times")
    #     ]
    # )

    # await dp.bot.set_my_commands()
