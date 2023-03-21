using System.Diagnostics;
using System.Windows.Threading;

namespace Stopky.Commands;

public class StopTimerCommand: CommandBase{
    private Stopwatch Timer;
    private DispatcherTimer Dispatcher;
    
    public StopTimerCommand(Stopwatch timer, DispatcherTimer dispatcher){
        Timer = timer;
        Dispatcher = dispatcher;
    }
    
    public override void Execute(object? parameter){
        if (Timer.IsRunning){  
            Timer.Stop();  
        }
    }
}