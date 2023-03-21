using System.Diagnostics;
using System.Windows.Threading;

namespace Stopky.Commands;

public class StartTimerCommand: CommandBase{
    private Stopwatch Timer;
    private DispatcherTimer Dispatcher;
    
    public StartTimerCommand(Stopwatch timer, DispatcherTimer dispatcher){
        Timer = timer;
        Dispatcher = dispatcher;
    }
    
    public override void Execute(object? parameter){
        Timer.Start();  
        Dispatcher.Start();
    }
}