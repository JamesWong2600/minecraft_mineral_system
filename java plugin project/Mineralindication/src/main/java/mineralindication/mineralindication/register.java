package mineralindication.mineralindication;

import org.bukkit.*;
import org.bukkit.block.Block;
import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.block.BlockBreakEvent;

import java.sql.*;
import java.util.Random;
import java.util.UUID;

public class register implements CommandExecutor {

    static final String mineral = "SELECT id, iron, coal, diamond FROM mineral";
    String usermineral = "SELECT id, UUID, username, password, money, copper, iron, redstone, gold, diamond, emerald FROM usermineral";
    private Mineralindication plugin;
    public register() {
        this.plugin = plugin;
    }

    int x= 0;
    Random random = new Random();
    public boolean onCommand(CommandSender sender, Command command, String label, String[] args) {
        final Player p = (Player) sender;
        UUID id = p.getUniqueId();
        String ID = String.valueOf(p);
        String q1 = "CraftPlayer{name=";
        String q2 = "}";
        String q3 = ID.replace(q1, "").replace(q2, "");
        String ip = Mineralindication.getMain().getConfig().getString("SQL.ip");
        String table = Mineralindication.getMain().getConfig().getString("SQL.table");
        String user = Mineralindication.getMain().getConfig().getString("SQL.user");
        String password = Mineralindication.getMain().getConfig().getString("SQL.password");
        String DB_DRIVER = "com.mysql.jdbc.Driver";
        String DB_URL = "jdbc:mysql://" + ip + "/" + table;
        String DB_USERNAME = user;
        String DB_PASSWORD = password;
        try(Connection conn1 = DriverManager.getConnection(DB_URL, DB_USERNAME, DB_PASSWORD);
            Statement stmt1 = conn1.createStatement();
            Statement stmt2 = conn1.createStatement();
            ResultSet rs = stmt2.executeQuery("SELECT MAX(id) FROM usermineral");
        ) {
            rs.next();
            int maxid = rs.getInt(1);
            maxid+=1;
            String sqldata = "INSERT INTO usermineral VALUES ("+maxid+", '"+id+"', '"+args[0]+"', '"+args[1]+"', 0, 0, 0, 0, 0, 0, 0, 0)";
            stmt1.executeUpdate(sqldata);
            p.sendMessage(ChatColor.GREEN + "SUCESSFUL CREATED AN BANK ACCOUNT，YOUR USERNAME IS "+args[0]+" YOUR PASSWORD IS "+args[1]);
            p.playSound(p.getLocation(), Sound.ENTITY_EXPERIENCE_ORB_PICKUP, 20, 1);
            }
        catch (SQLException ed) {
            ed.printStackTrace();
    }

        return false;}
}
